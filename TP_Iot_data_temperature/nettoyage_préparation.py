from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

class DataPreparation:
    def __init__(self, spark, file_path):
        self.spark = spark
        self.file_path = file_path

    def load_data(self):
        df = self.spark.read.csv(self.file_path, header=True)
        df = df.withColumn("timestamp", to_timestamp(col("noted_date"), "dd-MM-yyyy HH:mm"))
        return df

    def clean_duplicates(self, df):
        return df.dropDuplicates()

# Initialisation Spark
spark = SparkSession.builder.appName("IoT Temperature TP").getOrCreate()

# Utilisation
prep = DataPreparation(spark, "D:/Travaux/MasterLesson/M1/IotAgentAI/b3-c--training/TP_Iot_data_temperature/IOT-temp.csv")
df = prep.load_data()
df_clean = prep.clean_duplicates(df)
df_clean.show()
