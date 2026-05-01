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
    f = g / (m+1)
    return f

def hondt(data):
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
def hondt_main(data):
    validate_input(data)

    result = hondt(data)

    return result