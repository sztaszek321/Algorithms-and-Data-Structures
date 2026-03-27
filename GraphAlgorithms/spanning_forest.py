# 1. IMPORTS & SAMPLES/TESTCASES

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

sample_data3 = [
    ("a", "b", 3),
    ("a", "e", 1),
    ("b", "c", 5),
    ("b", "e", 4),
    ("c", "d", 2),
    ("e", "c", 6),
    ("e", "d", 7)
] #example from: https://pl.wikipedia.org/wiki/Algorytm_Kruskala

sample_data4 = {
    "A": {"B": 7, "D": 5},
    "B": {"C": 8, "D": 9, "E": 7},
    "C": {"E": 5},
    "D": {"E": 15, "F": 6},
    "E": {"F": 8, "G": 9},
    "F": {"G": 11},
    "G": {}
} #example from: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm

sample_data5 = {
    "a": {"b": 4, "e": 1, "f": 1},
    "b": {"c": 2, "e": 2},
    "c": {"d": 8},
    "d": {"e": 3, "f": 6},
    "e": {"f": 2},
    "f": {}
} #example from: lecture

# 2. DATA VALIDATION
def validate_input(data):
    if data is None:
        raise ValueError("Input cannot be None")

    if isinstance(data, list) :
        pass
    elif isinstance(data, dict) :
        pass
    else :
        raise ValueError("Invalid edge type, must be list or dict")

    return data


# 3. HELPER FUNCTIONS
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

def build_arr(edges):
    arr = dict()
    for node in edges:
        arr.update({node: {}})
    return arr

def prim(start, data):
    e: list = []
    k: list = []
    if isinstance(data, list) :
        e = list(list_to_dict(data).keys())
        k = sorted(data, key=lambda tup: tup[2])
    elif isinstance(data, dict) :
        e = list(data.keys())
        h = dict_to_list(data)
        k = sorted(h, key=lambda tup: tup[2])

    if start is None:
        start = e[0]

    res = []
    apexes = {start}

    while len(apexes) < len(e):
        chosen = None
        found = False
        for u, v, w in k:
            if (u not in apexes and v in apexes) or (v not in apexes and u in apexes):
                found = True
                apex = u if u not in apexes else v
                apexes.add(apex)
                chosen = (u, v, w)
                res.append(chosen)
                break
        if found:
            k.remove(chosen)
        else:
            raise Exception("Graph is not spójny")
    return res


# 4. MAIN ALGORITHM
def spanning_forest_main(start, sample):
    sample = validate_input(sample)

    result = prim(start, sample)
    print(result)

    return result