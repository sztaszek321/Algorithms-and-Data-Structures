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
        arr.update({node: {node}})
    return arr

def kruskal(data):
    e: list = []
    k: list = []
    if isinstance(data, list) :
        e = list(list_to_dict(data).keys())
        k = sorted(data, key=lambda tup: tup[2])
    elif isinstance(data, dict) :
        e = list(data.keys())
        h = dict_to_list(data)
        k = sorted(h, key=lambda tup: tup[2])

    tree = build_arr(e)
    res = []
    n = len(e)

    while k and len(res) < n - 1:
        u, v, w = k.pop(0)

        if not bool(tree[u] & tree[v]):
            merged = tree[u] | tree[v]
            for apx in merged:
                tree[apx] = merged
            res.append((u, v, w))

    return res


# 4. MAIN ALGORITHM
def kruskal_main(sample):
    sample = validate_input(sample)

    result = kruskal(sample)
    print(result)

    return result
