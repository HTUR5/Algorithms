from typing import List

import networkx as nx


def find_cycle_in_consumption_graph(allocation: List[List[float]]):
    G = nx.Graph()
    numberOfPlayers = len(allocation)
    numberOfItems = len(allocation[0])
    for player in range(numberOfPlayers):
        G.add_node(("p", player))  # p is person
        for item in range(numberOfItems):
            if item == 0:
                G.add_node(("i", item))  # i is item
            if 0 < allocation[player][item] <= 1:
                G.add_edge(("p", player), ("i", item))
    try:
        print(list(nx.find_cycle(G, orientation="ignore")))
    except:
        print("no cycles")


if __name__ == '__main__':
    find_cycle_in_consumption_graph([[1, 0.7, 0.4, 0], [0, 0.3, 0.6, 1]])
    find_cycle_in_consumption_graph([[1, 0.4, 0, 0], [0, 0.6, 1, 1]])
