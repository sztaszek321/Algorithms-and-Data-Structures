# 1. IMPORTS & SAMPLES/TESTCASES
from tabulate import tabulate

sample_data1 = ("A", {
    "A": {"B": 4, "C": 1},
    "B": {"D": 2, "E": 5},
    "C": {"B": 2, "D": 8},
    "D": {"E": 1},
    "E": {}
})

sample_data2 = ("A", [
    ("A", "B", 4),
    ("A", "C", 1),
    ("B", "D", 2),
    ("B", "E", 5),
    ("C", "B", 2),
    ("C", "D", 8),
    ("D", "E", 1)
])

sample_data3 = ("0", {
    "0": {"1": 3, "4": 3},
    "1": {"2": 1},
    "2": {"3": 3, "5": 1},
    "3": {"1": 3},
    "4": {"5": 2},
    "5": {"0": 6, "3": 1}
})

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
        check_weight(edges)
    else :
        raise ValueError("Invalid edge type, must be list or dict")

    if start not in edges :
        raise ValueError("Invalid start node, must be in edges")

    return data


# 3. HELPER FUNCTIONS
def dict_to_list(edges: dict) -> list:
    edges_list = []
    for start, ends in edges.items():
        for e in ends:
            edges_list.append((start, e, ends[e]))
    return edges_list

def list_to_dict(edges: list) -> dict:
    edges_dict = dict()
    for start, end, weight in edges:
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        if start not in edges_dict:
            edges_dict[start] = {}
        if end not in edges_dict:
            edges_dict[end] = {}
        edges_dict[start][end] = weight
    return edges_dict

def check_weight(edges: dict):
    for start, end in edges.items():
        for e in end:
            if end[e] < 0:
                raise ValueError("Weight cannot be negative")

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

def dijkstra(start, edges):
    not_visited = set(edges.keys())
    arr = build_arr(start, edges)

    while not_visited:
        node = min(not_visited, key=lambda x: arr[x][0])
        not_visited.remove(node)

        for e in edges[node]:
            if e in not_visited:
                cost = arr[node][0] + edges[node][e]
                if cost < arr[e][0]:
                    arr[e] = [cost, node]
    return arr

# 4. MAIN ALGORITHM
def dijkstra_main(sample):
    sample = validate_input(sample)
    start = sample[0]
    edges = sample[1]

    result = dijkstra(start, edges)
    show_result(result)

    return result