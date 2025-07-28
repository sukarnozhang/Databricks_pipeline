# Step 1 - Establish AWS connections
def establish_aws_connection(spark):
    # Step 1: Get AWS credentials from Databricks Secrets
    aws_access_key = dbutils.secrets.get(scope="aws-secrets", key="aws-access-key")
    aws_secret_key = dbutils.secrets.get(scope="aws-secrets", key="aws-secret-key")

    # Step 2: Initialize boto3 client for S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )

    return s3

# Step 2 - create tracking tables for files which have been ingested
def create_ingested_files_log(tracking_table):
    # Define schema for tracking table
    tracking_table_schema = StructType([
        StructField("file_name", StringType(), False),
        StructField("ingestion_time", TimestampType(), False)
    ])

    # Create an empty DataFrame with this schema
    empty_df = spark.createDataFrame([], tracking_table_schema)

    # Check if table exists
    if not spark.catalog.tableExists(tracking_table):
        empty_df.write.format("delta").saveAsTable(tracking_table)
        print("Tracking table created.")
    else:
        print("Tracking table already exists.")

# Step 3: Get already ingested file names
def get_ingested_files(tracking_table):
    try:
        ingested_files = set(row["file_name"] for row in spark.table(tracking_table).collect())
    except:
        ingested_files = set()
        print("Tracking table not found. Assuming no files ingested yet.")
    return ingested_files