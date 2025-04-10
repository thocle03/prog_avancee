import pandas as pd

nom_fichier = './IOT-temp.csv'
df = pd.read_csv(nom_fichier)
print(df)

print("Nombre de doublons :", df.duplicated().sum())

df = df.drop_duplicates()

df['noted_date'] = pd.to_datetime(df['noted_date'])