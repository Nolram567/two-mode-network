import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from networkx.algorithms import bipartite
from networkx.algorithms import centrality

if __name__ == '__main__':

    df = pd.read_csv("Soziomatrix - Tabellenblatt1.csv")

    G = nx.Graph()

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


    '''print(list(individuals.keys()))
    print(opportunities)'''

    G.add_nodes_from(list(individuals.keys()), bipartite=0)
    G.add_nodes_from(opportunities, bipartite=1)


    for i in individuals.keys():
        for o, e in list(individuals[i].items()):

            if e == 1:
                edgelist.append((i, o))

    G.add_edges_from(edgelist)

    pos1 = nx.bipartite_layout(G, nodes=list(individuals.keys()))
    pos2 = nx.spring_layout(G)
    nx.draw(G, pos1, with_labels=True, font_weight='bold', node_size=700,
            node_color=['skyblue' if n in ['Cafè Wertvoll', 'VB Kletterhalle', 'Resteraunt Dromedar', 'Cavete', 'Cineplex',
                                           'Basic Coffee', 'Restaurant Mon Ami', 'Waggonhalle']
                        else 'salmon' for n in G.nodes()])

    plt.title('Bipartiter Graph')
    plt.show()


    #print(bipartite.clustering(G, list(G.nodes)[0:10:None]))
    G = nx.bipartite.projected_graph(G, list(G.nodes)[0:10:None])

    print(f"degree centrality : {centrality.degree_centrality(G)}\n")
    print(f"betweenness centrality : {centrality.betweenness_centrality(G)}\n")
    print(f"closeness centrality : {centrality.closeness_centrality(G)}\n")

    # Zeige den unipartiten Graphen
    nx.draw(G, with_labels=True, font_weight='bold', node_color='skyblue')
    plt.show()

    min_shared_opps = 3

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

    nx.draw(G_unimodal, pos, with_labels=True, font_weight='bold', node_size=700)

    print(f"degree centrality : {centrality.degree_centrality(G_unimodal)}\n")
    print(f"betweenness centrality : {centrality.betweenness_centrality(G_unimodal)}\n")
    print(f"closeness centrality : {centrality.closeness_centrality(G_unimodal)}\n")

    plt.show()



