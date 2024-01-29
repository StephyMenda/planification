class racordement:
    # Constructeur de la classe
    def __init__(self, data):
        self.data = data
    def priority_order(self):
        # Compter les occurrences de chaque valeur dans la colonne infra_id
        occurrences = self.data['infra_id'].value_counts()
        # Ajouter une colonne 'occurrences' au DataFrame
        self.data['occurrences'] = self.data['infra_id'].map(occurrences)
        # Trier le DataFrame par ordre décroissant d'occurrences et par 'infra_id'
        data_sorted = self.data.sort_values(by=['occurrences', 'infra_id'], ascending=[False, True])

        # Afficher le DataFrame trié
        return  data_sorted
        print(data_sorted)

        """Proposez un plan d'action qui détaille l'ordre dans lequel les bâtiments doivent être raccordés.
               Optimisation:
               Identifiez les opportunités de mutualisation des lignes pour réduire les coûts.
               Ajustez votre plan pour maximiser le nombre de prises raccordées.
               """

    def plan(self, data):
        self
        #a definir