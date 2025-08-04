from aws.s3_client import get_s3_client
#from config.config_loader import load_config
from spark.session import get_spark_session
#from spark.table_utils import create_table, get_last_ingested_time
#from pipeline.processor import process_s3_data
#from schemas.schema_definition import files_tracking_schema, last_ingested_times_schema, main_schema

# Initialize Spark session
spark = get_spark_session()

# AWS client
s3 = get_s3_client()

# Load config
config = load_config("config.txt")
bucket = config["bucket"]
prefix = config["prefix"]
files_tracking_table = config["files_tracking"]
last_ingested_table = config["last_ingested_times"]

# Create necessary tracking tables
create_table(spark, files_tracking_table, files_tracking_schema)
create_table(spark, last_ingested_table, last_ingested_times_schema)

# Get last ingested timestamp
last_ingested_time = get_last_ingested_time(spark, last_ingested_table)

# Ingest and process new files
process_s3_data(
    spark,
    s3,
    bucket,
    prefix,
    files_tracking_table,
    last_ingested_table,
    last_ingested_time,
    files_tracking_schema,
    main_schema
)
