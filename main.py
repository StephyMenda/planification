from graphe import graphe
from metrique import metrique
from racordement import racordement
if __name__ == '__main__':
    reseau=metrique("C:\\Hetic\\MD4\\python\\projet\\planification\\data\\reseau_en_arbre.csv")
    data = reseau.priorisation()
    graphe=graphe(data)
    data_prioriser=racordement(data)
    data_prioriser.priority_order()
    #graphe.modelisation()
    #print(reseau)