from pyspark.sql import SparkSession

def get_spark_session():
    return SparkSession.builder.appName("S3_JSON_Loader").getOrCreate()
