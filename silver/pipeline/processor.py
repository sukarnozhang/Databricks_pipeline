import json
from datetime import datetime, timezone
from pyspark.sql import Row
from botocore.exceptions import NoCredentialsError

def process_s3_data(spark, s3, bucket, prefix, files_tracking, last_ingested_table,
                    last_ingested_time, files_tracking_schema, main_schema):
    
    all_data = []
    new_files = []

    try:
        response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
        for obj in response.get('Contents', []):
            key = obj['Key']
            last_modified = obj['LastModified']
            if key.endswith(".json") and last_modified > last_ingested_time:
                file_obj = s3.get_object(Bucket=bucket, Key=key)
                data = json.loads(file_obj['Body'].read().decode('utf-8'))
                all_data.append(data)
                new_files.append((key, datetime.now(timezone.utc)))

    except NoCredentialsError:
        print("No AWS credentials found!")
        return

    if not all_data:
        print("No new files to process.")
        return

    # Save new data
    silver_df = spark.createDataFrame(all_data, schema=main_schema)
    silver_df.write.format("delta").mode("append").saveAsTable("workspace.silver_schema.silver_delta_table")

    # Update file tracking
    new_files_df = spark.createDataFrame(new_files, schema=files_tracking_schema)
    new_files_df.write.format("delta").mode("append").saveAsTable(files_tracking)

    # Update last ingested time
    latest_time = max(time for _, time in new_files)
    new_time_row = Row(last_ingested_times=latest_time)
    new_time_df = spark.createDataFrame([new_time_row])
    new_time_df.write.format("delta").mode("overwrite").saveAsTable(last_ingested_table)

    print(f"Ingested {len(new_files)} files. Updated last_ingested_times.")
