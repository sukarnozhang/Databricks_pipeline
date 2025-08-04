from pyspark.sql.types import *

# Define schema for JSON
main_schema = StructType([
    StructField("time", StringType(), False),
    StructField("systems", StructType([
        StructField("equipment_id", StringType(), False),
        StructField("component", StructType([
            StructField("columns", StructType([
                StructField("column_id", StringType(), False)
            ]), False)
        ]), False),
        StructField("im_id", StringType(), False)
    ]), False),

    StructField("users", StructType([
        StructField("my_submit", StructType([
            StructField("id", StringType(), False),
            StructField("datetime", StringType(), False)
        ]), False),
        StructField("my_review", StructType([
            StructField("id", StringType(), False),
            StructField("datetime", StringType(), False)
        ]), False),
        StructField("my_approval", StructType([
            StructField("id", StringType(), False),
            StructField("datetime", StringType(), False)
        ]), False),
        StructField("my_status", StructType([
            StructField("status", StringType(), False)
        ]), False)
    ]), False),

    StructField("methods", StructType([
        StructField("sop", StringType(), False),
        StructField("id", StringType(), False),
        StructField("meth_id", StringType(), False),
        StructField("temp_id", StringType(), False),
        StructField("report_template_version", StringType(), False),
        StructField("seq_id", StringType(), False),
        StructField("seq_version", StringType(), False)
    ]), False),

    StructField("runs", ArrayType(StructType([
        StructField("in_num", StringType(), False),
        StructField("in_name", StringType(), False),
        StructField("pk", StringType(), False)
    ])), False),

    StructField("sst", ArrayType(StructType([
        StructField("fk", StringType(), False),
        StructField("sst_res", StructType([
            StructField("number", StringType(), False),
            StructField("in_num", StringType(), False),
            StructField("in_name", StringType(), False),
            StructField("sst_name", StringType(), False),
            StructField("peak", StringType(), False),
            StructField("eval_result", StringType(), False),
            StructField("result", StringType(), False)
        ]), False)
    ])), False),

    StructField("results", ArrayType(StructType([
        StructField("fk", StringType(), False),
        StructField("result", StructType([
            StructField("samp_id", StringType(), False),
            StructField("as_id", StringType(), False),
            StructField("Type", StringType(), False),
            StructField("comp", StringType(), False),
            StructField("unit", StringType(), False),
            StructField("det_id", StringType(), False),
            StructField("result", StringType(), False),
            StructField("number_of_averaged_samples", StringType(), False)
        ]), False)
    ])), False)
])
files_tracking_schema = StructType([
    StructField("file_name", StringType(), False),
    StructField("ingestion_time", TimestampType(), False)
])

last_ingested_times_schema = StructType([
    StructField("last_ingested_times", TimestampType(), False)
])
