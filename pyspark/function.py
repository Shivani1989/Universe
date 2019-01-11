from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct, avg, stddev, format_number

spark=SparkSession.builder.appName('aggs').getOrCreate()

#Import File
file_location = "/FileStore/tables/sales_info.csv"
file_type = "csv"
df=spark.read.csv(file_location, inferSchema=True, header=True )

#Group By
df.groupby('Company').count().show()
df.agg({'Sales':'max'}).show()
group_data=df.groupby('Company')
group_data.agg({'Sales':'max'}).show()
df.select(avg('Sales')).show()
df.select(avg('Sales').alias('Average Sales')).show()
df.select(stddev('Sales')).show()
sales_std=df.select(stddev('Sales').alias('STD'))
sales_std.select(format_number('STD',2).alias('std')).show()

#Order By
df.orderBy('Sales').show()
df.orderBy(df['Sales'].desc()).show()
