# 1. IMPORTS & SAMPLES/TESTCASES
from tabulate import tabulate

sample_data1 = ("A", {
    "A": {"B": 4, "C": 1},
    "B": {"D": 2, "E": 5},
    "C": {"B": -2, "D": 8},
    "D": {"E": 1},
    "E": {}
})

sample_data2 = ("A", [
    ("A", "B", 4),
    ("A", "C", 1),
    ("B", "D", 2),
    ("B", "E", 5),
    ("C", "B", -2),
    ("C", "D", 8),
    ("D", "E", 1)
])

sample_data3 = ("A", {
    "A": {"F": 3, "B": 2, "D" : 5},
    "B": {"E": 1},
    "C": {"B": 7, "G": 4},
    "D": {"E": 1},
    "E": {"C": -3, "G": 3},
    "F": {"B": -4},
    "G": {"D": -1}
}) #example from: ByteQuest YT

# 2. DATA VALIDATION
def validate_input(data):
    if data is None:
        raise ValueError("Input cannot be None")

    if not isinstance(data[0], str):
        raise ValueError("Input start must be str")
    else:
        start = data[0]

    if isinstance(data[1], list) :
        edges = list_to_dict(data[1])
        data = (start, edges)
    elif isinstance(data[1], dict) :
        edges = data[1]
    else :
        raise ValueError("Invalid edge type, must be list or dict")

    if start not in edges :
        raise ValueError("Invalid start node, must be in edges")

    return data

# 3. HELPER FUNCTIONS
def build_arr(start, edges):
    arr = dict()
    for node in edges:
        d = 0 if start == node else float('inf')
        arr.update({node: [d, -1]})
    return arr

def show_result(arr):
    nodes = list(arr.keys())

    rows = [
        ["n"] + nodes,
        ["d"] + [arr[node][0] for node in nodes],
        ["p"] + [arr[node][1] for node in nodes],
    ]

    print(tabulate(rows, tablefmt="simple"))

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

def bellman_ford(start, edges):
    edges_list = dict_to_list(edges)
    arr = build_arr(start, edges)

    for i in range(len(edges) - 1):
        for u, v, w in edges_list:
            if arr[u][0] != float('inf'):
                cost = arr[u][0] + w
                if cost < arr[v][0]:
                    arr[v] = [cost, u]

    for u, v, w in edges_list:
        if arr[u][0] != float('inf') and arr[u][0] + w < arr[v][0]:
            raise ValueError("Graph contains a negative-weight cycle")

    return arr

# 4. MAIN ALGORITHM
def bellman_ford_main(sample):
    sample = validate_input(sample)
    start = sample[0]
    edges = sample[1]

    result = bellman_ford(start, edges)
    show_result(result)

    return result