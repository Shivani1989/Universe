import pyspark
df = sqlContext.sql("Select * from sales_info_csv")
df.show()
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('Basics').getOrCreate()
df = sqlContext.sql("Select * from people_json")
df.show()
df.printSchema()
df.columns
df.describe().show()
from pyspark.sql.types import (StructField, StringType,
                               IntegerType,StructType)
data_schema = [StructField('age', IntegerType(), True),
              StructField('Name', StringType(), True)]
final_struct = StructType(fields=data_schema)
df = spark.read.json('people_json', schema=final_struct)
df.printSchema()
