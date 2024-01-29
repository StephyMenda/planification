""" cette classe permet de transformer un data set( un fichier csv) en un graphe"""
###
 # Modélisez le réseau électrique en utilisant la théorie des graphes, où les bâtiments sont des nœuds et les lignes électriques sont des arêtes.
# Intégrez les données de coût dans les arêtes de votre modèle de graphe.
###
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
class graphe:
    # Constructeur de la classe
    def __init__(self, data):
        self.data = data

    def modelisation(self):
        #reseau = pd.read_csv(self.path)
        G = nx.Graph()
        # Ajouter les arêtes au graphe à partir du dataset (adaptez en fonction de votre structure CSV)
        for index, row in self.data.iterrows():
            G.add_edge(row['id_batiment'], row['infra_id'], weight=row['longueur'])
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', arrowsize=20)
        #nx.draw(G, pos, font_weight='bold', node_size=700, node_color='skyblue', arrowsize=20)

        # Ajouter les poids sur les arêtes
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Afficher le graphe
        plt.show()

