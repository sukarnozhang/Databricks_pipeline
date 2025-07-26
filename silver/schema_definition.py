from pyspark.sql.types import *

# Define schema for JSON
schema = StructType([
    StructField("time", StringType(), True),

    StructField("systems", StructType([
        StructField("equipment_id", StringType(), True),
        StructField("component", StructType([
            StructField("columns", StructType([
                StructField("column_id", StringType(), True)
            ]), True)
        ]), True),
        StructField("im_id", StringType(), True)
    ]), True),

    StructField("users", StructType([
        StructField("my_submit", StructType([
            StructField("id", StringType(), True),
            StructField("datetime", StringType(), True)
        ]), True),
        StructField("my_review", StructType([
            StructField("id", StringType(), True),
            StructField("datetime", StringType(), True)
        ]), True),
        StructField("my_approval", StructType([
            StructField("id", StringType(), True),
            StructField("datetime", StringType(), True)
        ]), True),
        StructField("my_status", StructType([
            StructField("status", StringType(), True)
        ]), True)
    ]), True),

    StructField("methods", StructType([
        StructField("sop", StringType(), True),
        StructField("id", StringType(), True),
        StructField("meth_id", StringType(), True),
        StructField("temp_id", StringType(), True),
        StructField("report_template_version", StringType(), True),
        StructField("seq_id", StringType(), True),
        StructField("seq_version", StringType(), True)
    ]), True),

    StructField("runs", ArrayType(StructType([
        StructField("in_num", StringType(), True),
        StructField("in_name", StringType(), True),
        StructField("pk", StringType(), True)
    ])), True),

    StructField("sst", ArrayType(StructType([
        StructField("fk", StringType(), True),
        StructField("sst_res", StructType([
            StructField("number", StringType(), True),
            StructField("in_num", StringType(), True),
            StructField("in_name", StringType(), True),
            StructField("sst_name", StringType(), True),
            StructField("peak", StringType(), True),
            StructField("eval_result", StringType(), True),
            StructField("result", StringType(), True)
        ]), True)
    ])), True),

    StructField("results", ArrayType(StructType([
        StructField("fk", StringType(), True),
        StructField("result", StructType([
            StructField("samp_id", StringType(), True),
            StructField("as_id", StringType(), True),
            StructField("Type", StringType(), True),
            StructField("comp", StringType(), True),
            StructField("unit", StringType(), True),
            StructField("det_id", StringType(), True),
            StructField("result", StringType(), True),
            StructField("number_of_averaged_samples", StringType(), True)
        ]), True)
    ])), True)
])
