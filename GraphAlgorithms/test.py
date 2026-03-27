from GraphAlgorithms.kruskal_spanning_forest import kruskal_main
from GraphAlgorithms.spanning_forest import spanning_forest_main
from GraphAlgorithms.nearest_neighbour import nearest_neighbour_main
from GraphAlgorithms.dijkstra import dijkstra_main
from GraphAlgorithms.bellman_ford import bellman_ford_main
from GraphAlgorithms.johnson import johnson_main

""" 
-------------------------
2. GRAPH ALGORITHMS
-------------------------
"""

data_graph1 = ("B", {
    "A": {"B": 9, "C": 27, "D": 29},
    "B": {"A": 9, "D": 16, "E": 37},
    "C": {"A": 27, "D": 18, "F": 22},
    "D": {"A": 29, "B": 16, "C": 18, "E": 28, "F": 14, "G": 31},
    "E": {"B": 37, "D": 28, "F": 26, "G": 23},
    "F": {"C": 22, "D": 14, "E": 26, "G": 20},
    "G": {"D": 31, "E": 23, "F": 20}
})
data_graph2 = ("A", {
    "A": {"B": 3, "C": 2},
    "B": {"D": 1},
    "C": {"B": 5},
    "D": {"A": 9}
})

print("--- Nearest Neighbour ---")

datas = [data_graph1, data_graph2]

for data in datas:
    print(data)
    print(nearest_neighbour_main(data))
    print(" ")

data_Dij1 = ("A", [
    ("A", "B", 4),
    ("A", "C", 1),
    ("B", "D", 2),
    ("B", "E", 5),
    ("C", "B", 2),
    ("C", "D", 8),
    ("D", "E", 1)
])
data_Dij2 = ("0", {
    "0": {"1": 3, "4": 3},
    "1": {"2": 1},
    "2": {"3": 3, "5": 1},
    "3": {"1": 3},
    "4": {"5": 2},
    "5": {"0": 6, "3": 1}
})

print("--- Dijkstra ---")

data_dijkstra = [data_Dij1, data_Dij2]

for d in data_dijkstra:
    print(d)
    dijkstra_main(d)
    print(" ")

data_BF1 = ("A", [
    ("A", "B", 4),
    ("A", "C", 1),
    ("B", "D", 2),
    ("B", "E", 5),
    ("C", "B", -2),
    ("C", "D", 8),
    ("D", "E", 1)
])

data_BF2 = ("A", {
    "A": {"F": 3, "B": 2, "D" : 5},
    "B": {"E": 1},
    "C": {"B": 7, "G": 4},
    "D": {"E": 1},
    "E": {"C": -3, "G": 3},
    "F": {"B": -4},
    "G": {"D": -1}
}) #example from: ByteQuest YT

print("--- Bellman-Ford ---")

data_bellman_ford = [data_BF1, data_BF2]
data_bellman_ford.extend(data_dijkstra)

for d in data_bellman_ford:
    print(d)
    bellman_ford_main(d)
    print(" ")

data_Johnson1 = {
    "A": {"C": 5},
    "B": {"A": -4, "E": -1},
    "C": {"B": 3, "D": 15},
    "D": {},
    "E": {"C": 1, "D": -2}
} #example from: https://www.baeldung.com/cs/all-pairs-shortest-paths-johnsons-algorithm
data_Johnson2 = {
    "0": {"1": -5, "2": 2, "3": 3},
    "1": {"2": 4},
    "2": {"3": 1},
    "3": {}
} #example from: https://www.geeksforgeeks.org/dsa/johnsons-algorithm/

print("--- Johnson ---")

data_johnson = [data_Johnson1, data_Johnson2]

for k, e in data_bellman_ford:
    data_johnson.append(e)

for d in data_johnson:
    print(d)
    johnson_main(d)
    print(" ")

data_kruskal_and_prim1 = [
    ("a", "b", 3),
    ("a", "e", 1),
    ("b", "c", 5),
    ("b", "e", 4),
    ("c", "d", 2),
    ("e", "c", 6),
    ("e", "d", 7)
] #example from: https://pl.wikipedia.org/wiki/Algorytm_Kruskala

data_kruskal_and_prim2 = {
    "A": {"B": 7, "D": 5},
    "B": {"C": 8, "D": 9, "E": 7},
    "C": {"E": 5},
    "D": {"E": 15, "F": 6},
    "E": {"F": 8, "G": 9},
    "F": {"G": 11},
    "G": {}
} #example from: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm

data_kruskal_and_prim3 = {
    "a": {"b": 4, "e": 1, "f": 1},
    "b": {"c": 2, "e": 2},
    "c": {"d": 8},
    "d": {"e": 3, "f": 6},
    "e": {"f": 2},
    "f": {}
} #example from: lecture

print("--- Kruskal ---")

data_k_p = [data_kruskal_and_prim1, data_kruskal_and_prim2, data_kruskal_and_prim3]

for d in data_k_p:
    print(d)
    kruskal_main(d)
    print(" ")

print("--- Prim ---")

for d in data_k_p:
    print(d)
    spanning_forest_main(None, d)
    print(" ")


