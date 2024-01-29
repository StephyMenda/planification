import geopandas as gpd
import matplotlib .pyplot as plt
import pandas as pd

# Remplacez 'chemin/vers/votre/fichier.shp' par le chemin de votre propre fichier shapefile
path = 'C:\\Hetic\\MD4\\python\\projet\\planification\\data\\infrastructures.shp'

# Charger le fichier shapefile en un GeoDataFrame
infrastructure = gpd.read_file(path)
#gdf.plot()
#plt.show()
# Afficher les premières lignes du GeoDataFrame
# print(infrastructure)
batiment = gpd.read_file("C:\\Hetic\\MD4\\python\\projet\\planification\\data\\batiments.shp")
reseau = pd.read_csv("C:\\Hetic\\MD4\\python\\projet\\planification\\data\\reseau_en_arbre.csv")
infrastructure= gpd.read_file("C:\\Hetic\\MD4\\python\\projet\\planification\\data\\infrastructures.shp")
print(reseau)
print(infrastructure)
#print(batiment.head())
print(infrastructure.head())
# Grouper par la colonne 1 et compter le nombre de lignes dans chaque groupe
result = reseau.groupby('infra_id').size().reset_index(name='Nombre_de_lignes')

# Afficher le résultat
print(result)

