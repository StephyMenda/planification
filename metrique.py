import pandas as pd

 # Définition d'une fonction de mapping pour attribuer un poids numérique à chaque valeur du infra_type
def map_infrastructure(x):
    if x == 'infra_intacte':
        return 1
    elif x == 'a_remplacer':
        return 2
class metrique:
    # Constructeur de la classe
    def __init__(self, path):
        self.path = path

    def priorisation(self):

       df = pd.read_csv(self.path)
       # Appliquer la fonction de mapping à la colonne FacteurInfluence pour créer une colonne PoidsInfluence
       df['infra_prio'] = df['infra_type'].map(map_infrastructure)

       # Tri du DataFrame par la colonne correspondante, la colonne des coûts, et la colonne des poids d'influence
       df = df.sort_values(by=['id_batiment', 'infra_prio', 'longueur'])

       # Suppression des doublons basés sur la colonne correspondante
       df = df.drop_duplicates(subset='id_batiment', keep='first')
       return df
       print(df)