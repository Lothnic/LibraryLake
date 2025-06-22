from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("LibraryLake").getOrCreate()

df = spark.read.csv('data/books.csv')

