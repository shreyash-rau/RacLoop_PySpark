
# code at the beginning of your script to initialize findspark:

import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, pow

# Initialize Spark session
spark = SparkSession.builder.appName("HeartDiseasePreprocessing").getOrCreate()

# Load the dataset
df = spark.read.csv("Data_set.csv", header=True, inferSchema=True)

# One-Hot Encoding for 'cp' (chest pain type)
df = df.withColumn("cp_0", when(col("cp") == 0, 1).otherwise(0)) \
       .withColumn("cp_1", when(col("cp") == 1, 1).otherwise(0)) \
       .withColumn("cp_2", when(col("cp") == 2, 1).otherwise(0)) \
       .withColumn("cp_3", when(col("cp") == 3, 1).otherwise(0))

# Feature Derivation: powerOfTrestbps
df = df.withColumn("powerOfTrestbps", pow(col("trestbps"), 2))

# Data Filtering: Patients older than 50 years with resting blood pressure > 140
df_filtered = df.filter((col("age") > 50) & (col("trestbps") > 140))

# Quantization of Cholesterol Levels
df_filtered = df_filtered.withColumn("cholesterol_level", 
                                     when(col("chol") < 200, "Low")
                                     .when((col("chol") >= 200) & (col("chol") <= 239), "Medium")
                                     .otherwise("High"))

# Data Reduction: Count patients with "High" cholesterol level
high_chol_count = df_filtered.filter(col("cholesterol_level") == "High").count()
print(f"Number of patients with high cholesterol: {high_chol_count}")

# Save the pre-processed dataset to a CSV file
df_filtered.write.csv("preprocessed_heart_disease.csv", header=True)

# Stop the Spark session
spark.stop()
