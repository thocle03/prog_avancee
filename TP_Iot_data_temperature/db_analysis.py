from pyspark.sql.functions import avg, max, min, count, hour
from nettoyage_préparation import df_clean

class BasicAnalysis:
    def __init__(self, df):
        self.df = df

    def count_in_out_per_minute(self):
        return self.df.groupBy("noted_date", "out/in").agg(count("*").alias("count"))

    def avg_temp_by_direction(self):
        return self.df.groupBy("out/in").agg(avg("temp").alias("average_temp"))

    def temp_extremes(self):
        max_temp = self.df.agg(max("temp")).collect()[0][0]
        min_temp = self.df.agg(min("temp")).collect()[0][0]
        return max_temp, min_temp

# Analyse
analysis = BasicAnalysis(df_clean)
analysis.count_in_out_per_minute().show()
analysis.avg_temp_by_direction().show()
print("Temp Max/Min:", analysis.temp_extremes())
