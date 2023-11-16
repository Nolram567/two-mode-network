import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

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
    #print(individuals["Name IX"].iloc[0])

    for i in individuals.keys():
        for o, e in list(individuals[i].items()):

            if e == 1:
                edgelist.append((i, o))

    G.add_edges_from(edgelist)

    pos = nx.bipartite_layout(G, nodes=list(individuals.keys()))  # bipartite_layout zur Positionierung der Knoten
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, cmap=plt.cm.Paired)
    plt.title('Bipartiter Graph')
    plt.show()

