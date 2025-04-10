# TP5 - Analyse de données IoT d'un capteur de température

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Partie 1 : Nettoyage et préparation des données

# Charger le fichier CSV (même dossier que le script)
nom_fichier = 'IOT-temp.csv'
  # Remplacer par ton fichier CSV

df = pd.read_csv(nom_fichier)

# Afficher les premières lignes pour vérification
print("Aperçu des données :\n", df.head())

# Vérifier les doublons
print("Nombre de doublons :", df.duplicated().sum())

# Supprimer les doublons
df = df.drop_duplicates()

# Convertir la colonne 'noted_date' en datetime
df['noted_date'] = pd.to_datetime(df['noted_date'])

# Partie 2 : Analyse de base

# Compter le nombre d'entrées et de sorties par minute
df['minute'] = df['noted_date'].dt.floor('T')  # Arrondi à la minute
compte_in_out = df.groupby(['minute', 'out/in']).size().unstack(fill_value=0)
print("\nNombre d'entrées/sorties par minute :\n", compte_in_out)

# Température moyenne pendant les entrées et sorties
temp_moyenne = df.groupby('out/in')['temp'].mean()
print("\nTempérature moyenne lors des entrées et sorties :\n", temp_moyenne)

# Température maximale et minimale
temp_max = df.loc[df['temp'].idxmax()]
temp_min = df.loc[df['temp'].idxmin()]

print(f"\nTempérature maximale : {temp_max['temp']} °C à {temp_max['noted_date']}")
print(f"Température minimale : {temp_min['temp']} °C à {temp_min['noted_date']}")

# Partie 3 : Détection d'anomalies

# Seuil critique
seuil_temp = 40  # °C
anomalies = df[df['temp'] > seuil_temp]

print("\nAnomalies (temp > 40°C) :\n", anomalies)

# Action automatique simulée
def alerte_temperature(row):
    print(f"ALERTE : Température critique de {row['temp']} °C détectée le {row['noted_date']}")

# Appliquer l'alerte
anomalies.apply(alerte_temperature, axis=1)

# Partie 4 : Visualisation

plt.figure(figsize=(14, 7))
sns.lineplot(data=df, x='noted_date', y='temp', label='Température')

# Marquer les entrées/sorties
in_events = df[df['out/in'] == 'In']
out_events = df[df['out/in'] == 'Out']

plt.scatter(in_events['noted_date'], in_events['temp'], color='green', label='Entrée', marker='^')
plt.scatter(out_events['noted_date'], out_events['temp'], color='red', label='Sortie', marker='v')

# Ligne de seuil critique
plt.axhline(seuil_temp, color='r', linestyle='--', label='Seuil critique')

plt.title('Evolution de la température et événements In/Out')
plt.xlabel('Date/Heure')
plt.ylabel('Température (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()