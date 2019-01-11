from pyspark.sql import SparkSession
Spark= SparkSession.builder.appName('Dates').getOrCreate()

file_location = "/FileStore/tables/appl_stock.csv"
df=Spark.read.csv(file_location, header=True, inferSchema=True)

from pyspark.sql.functions import (dayofmonth, hour, dayofyear, month, year, weekofyear, format_number, date_format)

#df.select(year(df['Date'])).show()
newdf= df.withColumn('Year', year(df['Date']))
result= newdf.groupBy('Year').mean().select('Year', 'avg(Close)')
result.withColumnRenamed('avg(Close)', 'Average_Closing_Price').select(['Year', format_number('Average_Closing_Price', 2).alias('Average Close')]).show()
