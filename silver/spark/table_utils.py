from datetime import datetime, timezone
from pyspark.sql import Row

def create_table(spark, table_name, schema):
    if not spark.catalog.tableExists(table_name):
        empty_df = spark.createDataFrame([], schema)
        empty_df.write.format("delta").saveAsTable(table_name)

        if "last_ingested_times" in table_name:
            default_time = datetime(1900, 1, 1, tzinfo=timezone.utc)
            row = Row(last_ingested_times=default_time)
            init_df = spark.createDataFrame([row], schema)
            init_df.write.format("delta").mode("append").saveAsTable(table_name)

def get_last_ingested_time(spark, table_name):
    df = spark.read.table(table_name)
    last_ts = df.collect()[0]["last_ingested_times"]
    if last_ts.tzinfo is None:
        last_ts = last_ts.replace(tzinfo=timezone.utc)
    return last_ts
