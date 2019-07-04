import pandas as pd
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession

sc = SparkContext('local')
spark = SparkSession(sc)

data = [['tom', 10], ['nick', 15], ['juil', 14]]
df = pd.DataFrame(data, columns = ['Name', 'Age'])

pyspark_df = spark.createDataFrame(df)

print(type(pyspark_df))