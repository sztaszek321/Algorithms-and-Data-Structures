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
def vote_factor(g, l, w):
    f = g*l / w
    return f

def h_n(data):
    m = data[0]
    p = data[1]
    g = data[2]
    w = sum(g)
    t = []
    factors = []
    for v in g:
        f = vote_factor(v, m, w)
        intf = int(f)
        t.append(int(f))
        factors.append(f-intf)

    for i in range(m-sum(t)):
        idx = factors.index(max(factors))
        t[idx] += 1
        factors[idx] = 0

    return t


# 4. MAIN ALGORITHM
def hare_niemeyer_main(data):
    validate_input(data)

    result = h_n(data)

    return result