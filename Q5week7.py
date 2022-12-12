from typing import List

import networkx as nx
import pulp as p


def rental_harmony(allocation: List[List[float]], R):
    #find perfect matching and return dict of that
    G = nx.Graph()
    numberOfPlayers = len(allocation)
    numberOfItems = len(allocation[0])
    edges = []
    for player in range(numberOfPlayers):
        for item in range(numberOfItems):
            edges.append((("p", player), ("i", item), allocation[player][item]))
    G.add_weighted_edges_from(edges)
    matching = nx.max_weight_matching(G)

    #order a dict so the key is the room and the value is the player
    dic_matching = {}
    for m in matching:
        if m[0][0] == "p":
            newM = (m[1][1], m[0][1])
            dic_matching[newM[0]] = newM[1]
        else:
            newM = (m[0][1], m[1][1])
            dic_matching[newM[0]] = newM[1]

    #linear programming to find the price for each room according to the rent price
    Lp_prob = p.LpProblem('Problem', p.LpMaximize)
    priceForRoom = []
    for i in range(numberOfPlayers):
        priceForRoom.append(p.LpVariable(str(i)))
    z = p.LpVariable("z")
    for j in range(numberOfPlayers):
        for i in range(numberOfPlayers):
            Lp_prob += (allocation[dic_matching[j]][j] - priceForRoom[j]) >= (allocation[dic_matching[j]][i] - priceForRoom[i])
    for j in range(numberOfPlayers):
        Lp_prob += z <= (allocation[dic_matching[j]][j] - priceForRoom[j])
    total_price = 0
    for i in range(len(priceForRoom)):
        total_price += priceForRoom[i]
    Lp_prob += total_price == R
    status = Lp_prob.solve()
    print("dict of allocation: key is room and value is the player who got it")
    print(dic_matching)
    for i in range(numberOfPlayers):
        print("room" + str(i) + " " + str(priceForRoom[i].value()))





if __name__ == '__main__':
    print(rental_harmony([[25, 40, 25], [35, 60, 40], [25, 40, 20]], 2500))
    print(rental_harmony([[11, 22, 33], [44, 55, 66], [77, 88, 99]], 584707707))

