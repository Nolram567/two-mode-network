import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp

if __name__ == '__main__':

    df = pd.read_csv("Soziomatrix - Tabellenblatt1.csv")

    G = nx.DiGraph()

    individuals = {}
    opportunities = []
    edgelist = []


    for i, node in enumerate(df.columns):
        if i == 0:
            continue
        #print(node)
        opportunities.append(node)

    for row in df.index:
        individuals[df.iloc[row].iloc[0]] = df.iloc[row].iloc[1:]


    print(list(individuals.keys()))
    print(opportunities)

    G.add_nodes_from(list(individuals.keys()), bipartite=0)
    G.add_nodes_from(opportunities, bipartite=1)
    print(individuals["Name IX"].iloc[0])

    for i in individuals.keys():
        for o, e in list(individuals[i].items()):

            if e == 1:
                edgelist.append((i, o))

    G.add_edges_from(edgelist)

    pos = nx.bipartite_layout(G, nodes=list(individuals.keys()))  # bipartite_layout zur Positionierung der Knoten
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, cmap=plt.cm.Paired)
    plt.title('Bipartiter Graph')
    plt.show()

    min_shared_opps = 2

    G_unimodal = nx.Graph()
    edgelist_unimodal = []

    G_unimodal.add_nodes_from(list(individuals.keys()), bipartite=0)

    for i, indiv1 in enumerate(individuals.keys()):
        for j, indiv2 in enumerate(individuals.keys()):
            if i < j:  # Um Duplikate zu vermeiden
                shared_opps = set(individuals[indiv1].index[individuals[indiv1] == 1]) & set(
                    individuals[indiv2].index[individuals[indiv2] == 1])
                if len(shared_opps) >= min_shared_opps:
                    edgelist_unimodal.append((indiv1, indiv2, {'shared_opportunities': list(shared_opps)}))

    G_unimodal.add_edges_from(edgelist_unimodal)

    pos = nx.kamada_kawai_layout(G_unimodal)

    nx.draw(G_unimodal, pos, with_labels=True, font_weight='bold', node_size=700, cmap=plt.cm.Paired)

    plt.show()



