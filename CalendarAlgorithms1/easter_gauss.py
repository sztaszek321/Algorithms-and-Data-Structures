# 1. IMPORTS & SAMPLES/TESTCASES

sample_data = [1600, 1700, 1800, 1900, 1954, 1977, 1981, 1988, 1991, 2000, 2010, 2019, 2022, 2024, 2025, 2026, 2038, 2040, 2056]

# 2. DATA VALIDATION
def validate_input(year):
    if year is None:
        raise ValueError("Input cannot be None")
    if not isinstance(year, int):
        raise ValueError("Input must be int")
    if year > 2499:
        raise ValueError("Input must be smaller than or equal to 2499")
    if year < 1583:
        raise ValueError("Input must be greater than or equal to 1583")

    return year


# 3. HELPER FUNCTIONS
def a_h(year):
    return year % 19

def b_h(year):
    return year % 4

def c_h(year):
    return year % 7

def AB_h(year):
    if year <= 1582:
        return 15, 6
    elif year <= 1699 :
        return 22, 2
    elif year <= 1799 :
        return 23, 3
    elif year <= 1899 :
        return 23, 4
    elif year <= 2099 :
        return 24, 5
    elif year <= 2199 :
        return 24, 6
    elif year <= 2299 :
        return 25, 0
    elif year <= 2399 :
        return 26, 1
    else:
        return 25, 1

def d_h(a, A):
    return (a * 19 + A) % 30

def e_h(b, c, d, B):
    return (2*b + 4*c + 6*d + B) % 7

def easter_G(year):
    a = a_h(year)
    b = b_h(year)
    c = c_h(year)
    A, B = AB_h(year)
    d = d_h(a, A)
    e = e_h(b, c, d, B)

    if d == 29 and e == 6:
        easter = "19-04-" + str(year)
    elif d == 28 and e == 6:
        easter = "18-04-" + str(year)
    else:
        if d + e > 9:
            if d + e < 19:
                h = "0"
            else:
                h = ""
            easter = h + str(d + e - 9) + "-04-" + str(year)
        else:
            easter = str(22 + d + e) + "-03-" + str(year)

    return easter


# 4. MAIN ALGORITHM
def easter_gauss_main(year):
    validate_input(year)

    result = easter_G(year)

    return result