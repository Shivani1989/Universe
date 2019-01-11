from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('ops').getOrCreate()
# File location and type
file_location = "/FileStore/tables/appl_stock.csv"
file_type = "csv"

# CSV options
infer_schema = "True"
first_row_is_header = "True"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

display(df)
df.printSchema()
df.head(3)[0]
df.filter('Close<500').select(['Open', 'Close']).show()
df.filter(df['Close']<500).select('Volume').show()
df.filter( (df['Close']<200) & ~(df['Open']>200)).show()
result = df.filter(df['Low']==197.16).collect()
result[0].asDict()['Volume']
