# 1. IMPORTS & SAMPLES/TESTCASES
import copy

from tabulate import tabulate
from GraphAlgorithms.bellman_ford import bellman_ford
from GraphAlgorithms.dijkstra import dijkstra

sample_data1 = {
    "A": {"B": 4, "C": 1},
    "B": {"D": 2, "E": 5},
    "C": {"B": -2, "D": 8},
    "D": {"E": 1},
    "E": {}
}

sample_data2 = [
    ("A", "B", 4),
    ("A", "C", 1),
    ("B", "D", 2),
    ("B", "E", 5),
    ("C", "B", -2),
    ("C", "D", 8),
    ("D", "E", 1)
]

sample_data3 = {
    "A": {"F": 3, "B": 2, "D" : 5},
    "B": {"E": 1},
    "C": {"B": 7, "G": 4},
    "D": {"E": 1},
    "E": {"C": -3, "G": 3},
    "F": {"B": -4},
    "G": {"D": -1}
} #example from: ByteQuest YT

sample_data4 = {
    "0": {"1": -5, "2": 2, "3": 3},
    "1": {"2": 4},
    "2": {"3": 1},
    "3": {}
}

sample_data5 = {
    "A": {"C": 5},
    "B": {"A": -4, "E": -1},
    "C": {"B": 3, "D": 15},
    "D": {},
    "E": {"C": 1, "D": -2}
} #example from: https://www.baeldung.com/cs/all-pairs-shortest-paths-johnsons-algorithm

# 2. DATA VALIDATION
def validate_input(data):
    if data is None:
        raise ValueError("Input cannot be None")

    if isinstance(data, list) :
        edges = list_to_dict(data)
        data = edges
    elif isinstance(data, dict) :
        edges = data
    else :
        raise ValueError("Invalid edge type, must be list or dict")

    return data

# 3. HELPER FUNCTIONS
def build_arr(start, edges):
    arr = dict()
    for node in edges:
        d = 0 if start == node else float('inf')
        arr.update({node: [d, -1]})
    return arr

def show_arr(arr):
    for node in arr:
        print(node, end='   ')
    print("")
    for node in arr:
        print(arr[node][0], end='   ')
    print("")
    for node in arr:
        print(arr[node][1], end='   ')
    print("")

def dict_to_list(edges) -> list:
    edges_list = []
    for start, ends in edges.items():
        for e in ends:
            edges_list.append((start, e, ends[e]))
    return edges_list

def list_to_dict(edges) -> dict:
    edges_dict = dict()
    for start, end, weight in edges:
        if start not in edges_dict:
            edges_dict[start] = {}
        if end not in edges_dict:
            edges_dict[end] = {}
        edges_dict[start][end] = weight

    return edges_dict

def new_apex(edges: dict):
    edges_q = copy.deepcopy(edges)
    edges_q.update({"q": {}})
    for e in edges_q:
        if e == "q":
            continue
        edges_q["q"].update({e: 0})
    return edges_q

def new_weights(edges: dict, arr):
    new_edges = dict()
    for u, ends in edges.items():
        new_edges.update({u: {}})
        for v in ends:
            new_weight = ends[v] + arr[u][0] - arr[v][0]
            new_edges[u].update({v: new_weight})
    return new_edges

def new_weights2(s, edges: dict, arr):
    new_edges = dict()
    weights = dict()
    for t, ends in edges.items():
        if s == t: # or ends[1] = -1
            new_weight = 0
        else:
            new_weight = ends[0] - arr[s][0] + arr[t][0]
        weights.update({t: new_weight})
    new_edges.update({s: weights})
    #print(new_edges)
    return new_edges

def show_result(result: list):
    rows = []
    col_names = None

    for el in result:
        for e, v in el.items():
            if col_names is None:
                col_names = list(v.keys())
            rows.append([e] + [v[col] for col in col_names])

    print(tabulate(rows, headers=[""] + col_names, tablefmt="simple"))

def johnson(data):
    edges = data

    #new apex q
    edges_q = new_apex(edges)

    #belmann-ford with q
    arr = bellman_ford("q", edges_q)

    #new edges
    edges_new = new_weights(edges, arr)

    #Dijsktra for new edges from every Apex
    edges_dij = dict()
    for apex in edges:
        edges_dij.update({apex: dijkstra(apex, edges_new)})

    #Change to correct weights
    res = []
    arr.pop("q")
    for apex in edges_dij:
        res.append(new_weights2(apex, edges_dij[apex], arr))

    return res

# 4. MAIN ALGORITHM
def johnson_main(sample):
    sample = validate_input(sample)

    result = johnson(sample)
    show_result(result)

    return result