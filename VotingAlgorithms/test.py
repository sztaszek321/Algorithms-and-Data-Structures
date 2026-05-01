from VotingAlgorithms.hare_niemeyer import hare_niemeyer_main
from VotingAlgorithms.hondt import hondt_main
from VotingAlgorithms.sainte_lague import sainte_lague_main

""" 
-------------------------
5. Voting Algorithms
-------------------------
"""

# [M - number of seats, P - number of parties, G - array containing votes cast for each party]

data_sample1 = [
    10,
    5,
    [34000, 28000, 16000, 6000, 3000]
]

data_sample2 = [
    5,
    3,
    [1000, 800, 300]
]

data_sample3 = [
    7,
    4,
    [5100, 5000, 4900, 4800]
]

data_sample4 = [
    15,
    6,
    [120000, 95000, 76000, 34000, 18000, 7000]
]

datas = [data_sample1, data_sample2, data_sample3, data_sample4]

for d in datas:
    print(d)
    print("--- saint-lague ---")
    print(sainte_lague_main(d))
    print("--- hare-niemeyer ---")
    print(hare_niemeyer_main(d))
    print("--- hondt ---")
    print(hondt_main(d))
    print("=============================")

