import pandas as pd
class infra:
    # Constructeur de la classe
    def __init__(self, path):
        self.path = path

    def repair_infra(self):
        df = pd.read_csv(self.path)
        return df.apply(lambda row: row['infra_type'] == "infra_intacte", axis=1)

    def get_infra_difficulty(self):
        df = pd.read_csv(self.path)
        pd.options.display.max_columns = None
        df['total_nb_maisons'] = df.groupby('infra_id')['nb_maisons'].transform('sum')
        df['difficulte_infra'] = df.apply(lambda row: row['longueur'] / row['total_nb_maisons'] if row['infra_type'] == "infra_intacte" else 0,axis=1)
        df.drop(columns=['total_nb_maisons'], inplace=True)
        return df

    def radd(self, id_batiment):
        df = self.get_infra_difficulty()
        liste_infra_par_batiment = []
        grouped = df.groupby('id_batiment')
        for batiment, group_data in grouped:
            if batiment == id_batiment:
                infra_tuples = [
                    (row['infra_id'], row['longueur'], row['difficulte_infra'], row['infra_type'], row['nb_maisons'])
                    for _, row in group_data.iterrows()]
                liste_infra_par_batiment.append((batiment, infra_tuples))
                break  # Arrêter la boucle après avoir trouvé les informations pour l'id_batiment spécifié
        return liste_infra_par_batiment





