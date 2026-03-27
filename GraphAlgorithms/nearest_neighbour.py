# 1. IMPORTS & SAMPLES/TEST CASES

""" ----- coordinates ----- """

sample_data1 = ("A" , {"A": (1, 1), "B": (2, 4), "C": (5, 5), "D": (6, 2), "E": (3, 0)}) # (starting point, coordinates of all points)

""" ----- directed graph ----- """

sample_data2 = ("A", [
    ("A", "B", 3),
    ("A", "C", 7),
    ("B", "D", 2),
    ("C", "B", 1),
    ("C", "D", 4),
    ("D", "E", 5),
    ("E", "A", 6)
]) # (starting point, edges)
sample_data3 = ("A", {
    "A": {"B": 3, "C": 7},
    "B": {"D": 2},
    "C": {"B": 1, "D": 4},
    "D": {"E": 5},
    "E": {"A": 6}
}) # (starting point, edges {from point: to points with weights})

""" ----- undirected graph ----- """

sample_data4 = ("A", [
    ("A", "B", 9),
    ("A", "C", 27),
    ("A", "D", 29),
    ("B", "D", 16),
    ("B", "E", 37),
    ("C", "D", 18),
    ("C", "F", 22),
    ("D", "E", 28),
    ("D", "F", 14),
    ("D", "G", 31),
    ("E", "G", 23),
    ("E", "F", 26),
    ("F", "G", 20)
]) # (starting point, edges)
sample_data5 = ("B", {
    "A": {"B": 9, "C": 27, "D": 29},
    "B": {"A": 9, "D": 16, "E": 37},
    "C": {"A": 27, "D": 18, "F": 22},
    "D": {"A": 29, "B": 16, "C": 18, "E": 28, "F": 14, "G": 31},
    "E": {"B": 37, "D": 28, "F": 26, "G": 23},
    "F": {"C": 22, "D": 14, "E": 26, "G": 20},
    "G": {"D": 31, "E": 23, "F": 20}
}) # (starting point, edges {from point: to points with weights})

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
        pass
    else :
        raise ValueError("Invalid edge type, must be list or dict")

    if start not in edges :
        raise ValueError("Invalid start node, must be in edges")

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

def nearest_neighbour(data):
    start = data[0]
    edges = data[1]

    path = str(start)
    track = 0

    not_visited = set(edges.keys())
    not_visited.remove(start)

    mod = 10 ** 9 + 7

    node = start

    while not_visited:
        pos_node = None
        cost = mod

        for e in edges[node]:
            if e in not_visited:
                if edges[node][e] < cost:
                    cost = edges[node][e]
                    pos_node = e

        if not pos_node:
            raise ValueError(f"Nearest neighbor cannot find a solution from node {node}")

        node = pos_node
        not_visited.remove(node)
        track += cost
        path += "-" + str(node)

    if start in edges[node]:
        path = path + "-" + str(start)
        track += edges[node][start]
    else:
        raise ValueError("Cannot close the cycle")

    return path, track


# 4. MAIN ALGORITHM
def nearest_neighbour_main(sample):
    sample = validate_input(sample)

    result = nearest_neighbour(sample)

    return result