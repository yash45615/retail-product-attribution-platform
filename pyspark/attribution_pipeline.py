from pyspark.sql import SparkSession

from pyspark.sql.functions import (
    col,
    lower,
    trim,
    concat_ws
)


spark = (
    SparkSession.builder
    .appName(
        "RetailProductAttribution"
    )
    .master("local[*]")
    .getOrCreate()
)


input_path = (
    "data/raw/products_100k.csv"
)


output_path = (
    "data/processed/"
    "pyspark_products"
)


df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv(input_path)
)


print(
    "Initial count:",
    df.count()
)


df = df.dropDuplicates(
    ["product_id"]
)


df = df.fillna({
    "title": "",
    "description": "",
    "brand": ""
})


df = df.withColumn(
    "title",
    trim(col("title"))
)


df = df.withColumn(
    "brand",
    lower(
        trim(
            col("brand")
        )
    )
)


df = df.withColumn(
    "search_text",
    lower(
        concat_ws(
            " ",
            col("title"),
            col("description"),
            col("brand")
        )
    )
)


print(
    "Clean count:",
    df.count()
)


df.select(
    "product_id",
    "title",
    "brand",
    "price"
).show(
    20,
    truncate=False
)


(
    df.write
    .mode("overwrite")
    .parquet(output_path)
)


print(
    "PySpark processing completed."
)


spark.stop()