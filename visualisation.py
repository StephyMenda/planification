import geopandas as gpd
import matplotlib .pyplot as plt
import pandas as pd

path = 'C:\\Hetic\\MD4\\python\\projet\\planification\\data\\infrastructures.shp'
reseau = pd.read_csv("C:\\Hetic\\MD4\\python\\projet\\planification\\data\\reseau_en_arbre.csv")
infrastructure= gpd.read_file("C:\\Hetic\\MD4\\python\\projet\\planification\\data\\infrastructures.shp")
print(reseau)
print(infrastructure)
#print(batiment.head())
#print(infrastructure.head())
# Trier les batiments afin de voir les infrastructures qui permettent de les racorder
result = reseau.groupby(by='id_batiment')
for id_batiment, result in result:
    print(id_batiment)
    print(result)
    print("+"*40)

