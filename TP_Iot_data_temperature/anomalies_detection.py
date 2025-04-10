from pyspark.sql.functions import col
from nettoyage_préparation import df_clean

class AnomalyDetector:
    def __init__(self, df, threshold=40):
        self.df = df
        self.threshold = threshold

    def detect(self):
        return self.df.filter(col("temp") > self.threshold)

# Anomalies
detector = AnomalyDetector(df_clean)
anomalies = detector.detect()
anomalies.show()
