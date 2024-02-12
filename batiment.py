import pandas as pd
from  infra import infra


class batiment:
    infra= infra("C:\\Hetic\\MD4\\python\\projet\\planification\\data\\reseau_en_arbre.csv")
    def __init__(self, infra):
        self.infra = infra

    def get_building_difficulty(self, id_batiment):
        infra_difficulty_list = self.infra.radd(id_batiment)
        difficulte_batiment = 0
        for batiment, infra_tuples in infra_difficulty_list:
            if batiment == id_batiment:
                difficulte_batiment += sum(
                    difficulte_infra for infra_id, longueur, difficulte_infra, infra_type, nb_maisons in infra_tuples)
                break
        return difficulte_batiment

    def badd(self):
        df = self.infra.get_infra_difficulty()
        df['difficulte_batiment'] = df['id_batiment'].apply(
            lambda id_batiment: self.get_building_difficulty(id_batiment))
        return df

    def list_batiment(self):
        df = self.badd()
        batiments_uniques = {}
        grouped = df.groupby('id_batiment')
        for id_batiment, group_data in grouped:
            difficulte = [(row['difficulte_batiment']) for index, row in group_data.iterrows()]
            # Utiliser un ensemble pour avoir des valeurs uniques
            batiments_uniques[id_batiment] = set(difficulte)
        # Convertir le dictionnaire en une liste de tuples
        liste_batiment_par_difficulte = list(batiments_uniques.items())
        return liste_batiment_par_difficulte
    def Lt(self):
        list=self.list_batiment()
        if len(list) != 0:
            next_batiment = min(list)
            return next_batiment




