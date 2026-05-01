# 1. IMPORTS & SAMPLES/TESTCASES

'''
[M - number of seats, P - number of parties, G - array containing votes cast for each party]
'''
data_sample1 = [
    10,
    5,
    [34000, 28000, 16000, 6000, 3000]
] #source: ChatGPT

data_sample2 = [
    5,
    3,
    [1000, 800, 300]
] #source: ChatGPT

data_sample3 = [
    7,
    4,
    [5100, 5000, 4900, 4800]
] #source: ChatGPT

data_sample4 = [
    15,
    6,
    [120000, 95000, 76000, 34000, 18000, 7000]
] #source: ChatGPT

data_norway = [
    169,
    9,
    [
        902296,  # Labour Party
        767903,  # Progress Party
        471602,  # Conservative Party
        181192,  # Socialist Left Party
        179994,  # Centre Party
        171342,  # Red Party
        152782,  # Green Party
        135230,  # Christian Democratic Party
        118941,  # Liberal Party
    ]
] # Norway 2025

data_new_zealand = [
    120,
    7,
    [
        1131501,  # National Party
        604535,   # Labour Party
        257359,   # Green Party
        208300,   # New Zealand First
        31849,    # Maori Party
        16689,    # ACT New Zealand
        5286      # United Future
    ]
] # new zealand 2014

# 2. DATA VALIDATION
def validate_input(sample_data):
    if len(sample_data) != 3:
        raise ValueError("Data must be of length 3")
    m = sample_data[0]
    p = sample_data[1]
    g = sample_data[2]
    if not isinstance(g, list):
        raise ValueError("Votes array must be of type list")
    if not isinstance(m, int):
        raise ValueError("M - Number of seats (1 value in data) must be of type int")
    if not isinstance(p, int):
        raise ValueError("P - Number of parties (2 value in data) must be of type int")
    if p != len(g):
        raise ValueError("Number of parties must be equal length of votes array")


# 3. HELPER FUNCTIONS
def vote_factor(g, m):
    f = g / (2*m+1)
    return f

def s_l(data):
    m = data[0]
    p = data[1]
    g = data[2]
    factors = g.copy()
    t = [0] * p

    for i in range(m):
        idx = factors.index(max(factors))
        t[idx] += 1
        factors[idx] = vote_factor(g[idx], t[idx])

    return t


# 4. MAIN ALGORITHM
def sainte_lague_main(data):
    validate_input(data)

    result = s_l(data)

    return result