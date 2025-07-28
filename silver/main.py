from schema_definition import schema
from processor import establish_aws_connection, create_ingested_files_log, get_ingested_files
import json
from botocore.exceptions import NoCredentialsError
from pyspark.sql import SparkSession
from datetime import datetime, timezone
from pyspark.sql.types import StructType, StructField, StringType, TimestampType


# Initialize Spark session
spark = SparkSession.builder.appName("S3_JSON_Loader").getOrCreate()

# Step 1 - Establish AWS connections
s3 = establish_aws_connection(spark)

# Step 2 - create tracking tables for files which have been ingested
tracking_table = "workspace.silver_schema.ingested_files_log"
create_ingested_files_log(tracking_table)

# Step 3: Get already ingested file names
ingested_files = get_ingested_files(tracking_table)





bucket = 'databricks-practice-sk'
prefix = 'raw_data/'





all_data = []
new_files_log = []

try:
    # Step 4: List all files in S3 prefix
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)

    for obj in response.get('Contents', []):
        key = obj['Key']
        last_modified = obj['LastModified']  # datetime in UTC

        if key.endswith('.json') and key not in ingested_files:
            # Download and parse
            file_obj = s3.get_object(Bucket=bucket, Key=key)
            json_data = file_obj['Body'].read().decode('utf-8')
            data_dict = json.loads(json_data)
            all_data.append(data_dict)

            # Log the file for tracking
            new_files_log.append((key, last_modified.isoformat(), datetime.now(timezone.utc).isoformat()))

    print(f"New JSON files to ingest: {len(new_files_log)}")

except NoCredentialsError:
    print("AWS credentials not found!")
    all_data = []

# Step 5: Create DataFrame and write to Delta
if all_data:
    silver_df = spark.createDataFrame(all_data, schema=schema)
    #silver_df.show(truncate=False)

    # Append new data
    silver_df.write.format("delta").mode("append").saveAsTable("workspace.silver_schema.silver_delta_table")
    print("New data appended to Delta table.")

    # Step 6: Update tracking table
    log_df = spark.createDataFrame(new_files_log, ["file_name", "last_modified", "ingested_at"])
    log_df.write.format("delta").mode("append").saveAsTable(tracking_table)
    print("Tracking table updated.")
else:
    print("No new files to process.")
