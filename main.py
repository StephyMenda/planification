from batiment import batiment
from infra import infra
import pandas as pd
from racordement import racordement
if __name__ == '__main__':
    reseau=infra("C:\\Hetic\\MD4\\python\\projet\\planification\\data\\reseau_en_arbre.csv")
    resultat_priorisation= reseau.get_infra_difficulty()
    batiment=batiment(reseau)
    list=reseau.radd("E000001")
    df=batiment.badd()
    liste=batiment.list_batiment()
    print(liste)
    #print(batiment.get_building_difficulty("E000381"))