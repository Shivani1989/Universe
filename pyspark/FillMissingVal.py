from pyspark.sql import SparkSession
Spark=SparkSession.builder.appName('miss').getOrCreate()

# File location and type
file_location = "/FileStore/tables/ContainsNull.csv"
file_type = "csv"
df=Spark.read.csv(file_location, header=True, inferSchema=True)

df.na.drop(thresh=2).show() #rows have atleast 2 non NULL values
df.na.drop(how='all').show() #drop only if all the values are NULL, default how -any
df.na.drop(subset=['Sales']).show() # drop if sales column has NULL values
df.na.fill('FILL VALUE').show() #filles varchar values
df.na.fill(0).show() #fill Integer values


from pyspark.sql.functions import mean
mean_val=df.select(mean(df['Sales'])).collect()
mean_sales=mean_val[0][0]
df.na.fill(mean_sales, ['Sales']).show() #replace null values with mean
df.na.fill(df.select(mean(df['Sales'])).collect()[0][0], ['Sales']).show() #combine all in one line
