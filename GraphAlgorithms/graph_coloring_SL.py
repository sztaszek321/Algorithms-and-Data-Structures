# 1. IMPORTS & SAMPLES/TESTCASES
import copy

sample_data1 = {
    "A": {"B", "C"},
    "B": {"D", "E"},
    "C": {"B", "D"},
    "D": {"E"},
    "E": {}
}

sample_data2 = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "B"),
    ("C", "D"),
    ("D", "E")
]

sample_data3 = [
    ("a", "b"),
    ("a", "f"),
    ("a", "g"),
    ("b", "c"),
    ("b", "g"),
    ("c", "d"),
    ("c", "g"),
    ("d", "e"),
    ("d", "g"),
    ("e", "f"),
    ("e", "g"),
    ("f", "g"),
] #example from: https://en.wikipedia.org/wiki/Recursive_largest_first_algorithm

sample_data4 = [
    ("a", "d"),
    ("a", "i"),
    ("b", "d"),
    ("c", "d"),
    ("c", "e"),
    ("c", "g"),
    ("d", "k"),
    ("d", "i"),
    ("d", "g"),
    ("d", "f"),
    ("d", "e"),
    ("e", "g"),
    ("g", "j"),
    ("h", "i"),
    ("j", "k"),
] #example from: lecture

sample_data5 = {
    "A": {"B", "C", "D"},
    "B": {"C", "E", "F", "G"},
    "C": {"D", "E"},
    "D": {"E"},
    "E": {"F", "G"},
    "F": {},
    "G": {},
} #example from: lecture

# 2. DATA VALIDATION
def validate_input(data):
    if data is None:
        raise ValueError("Input cannot be None")

    if isinstance(data, list) :
        pass
    elif isinstance(data, dict) :
        data = dict_to_list(data)
    else :
        raise ValueError("Invalid edge type, must be list or dict")

    return data


# 3. HELPER FUNCTIONS
def dict_to_list(edges) -> list:
    edges_list = []
    for start, ends in edges.items():
        for e in ends:
            edges_list.append((start, e))
    return edges_list

def list_to_dict(edges) -> dict:
    edges_dict = dict()
    for start, end in edges:
        if start not in edges_dict:
            edges_dict[start] = {}
        if end not in edges_dict:
            edges_dict[end] = {}

    return edges_dict

def delete_edges(vxs, apex):
    vxs.pop(apex, None)
    for k, v in vxs.items():
        if apex in v[1:]:
            v.remove(apex)
            v[0] -= 1
    return dict(sorted(vxs.items(), key=lambda item: item[1][0]))

def count_degree(edges):
    count = dict()
    for u, v in edges:
        if u in count:
            count[u][0] += 1
            count[u].append(v)
        else:
            count[u] = [1, v]
        if v in count:
            count[v][0] += 1
            count[v].append(u)
        else:
            count[v] = [1, u]
    return dict(sorted(count.items(), key=lambda item: item[1][0]))

def sl(data):
    vertexes = count_degree(data)
    cp = copy.deepcopy(vertexes)
    n = len(vertexes)
    colors = dict()
    deletes = []

    for i in range(n):
        apex = next(iter(cp))
        deletes.insert(0, apex)
        cp.pop(apex)
        cp = delete_edges(cp, apex)

    for v in deletes:
        flag = False
        for c, l in colors.items():
            if all(u not in vertexes[v][1:] for u in l):
                flag = True
                l.append(v)
                break
        if not flag:
            colors[len(colors) + 1] = [v]

    return colors

# 4. MAIN ALGORITHM
def sl_main(sample):
    sample = validate_input(sample)

    result = sl(sample)
    print(result)

    return result
