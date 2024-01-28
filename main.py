from graphe import graphe
from metrique import metrique
if __name__ == '__main__':
    reseau=metrique("C:\\Hetic\\MD4\\python\\projet\\planification\\data\\reseau_en_arbre.csv")
    reseau.priorisation()
    print(reseau)