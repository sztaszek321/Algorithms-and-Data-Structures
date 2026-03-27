# 1. IMPORTS & SAMPLES/TESTCASES

sample_data = [1600, 1700, 1800, 1900, 1954, 1977, 1981, 1988, 1991, 2000, 2010, 2019, 2022, 2024, 2025, 2026, 2038, 2040, 2056]

# 2. DATA VALIDATION
def validate_input(year):
    if year is None:
        raise ValueError("Input cannot be None")
    if not isinstance(year, int):
        raise ValueError("Input must be int")
    if year < 1583:
        raise ValueError("Input must be greater than or equal to 1583")

    return year


# 3. HELPER FUNCTIONS
def a_h(year):
    return year % 19

def b_h(year):
    return year // 100

def c_h(year):
    return year % 100

def d_h(b):
    return b // 4

def e_h(b):
    return b % 4

def f_h(b):
    return (b + 8) // 25

def g_h(b, f):
    return (b - f + 1) // 3

def h_h(a, b, d, g):
    return (19 * a + b - d - g + 15) % 30

def i_h(c):
    return c // 4

def k_h(c):
    return c % 4

def l_h(e, i, h, k):
    return (32 + 2 * e + 2 * i - h - k) % 7

def m_h(a, h, l):
    return (a + 11 * h + 22 * l) // 451

def p_h(h, l , m):
    return (h + l - 7 * m + 114) % 31

def day_h(p):
    day = str(p + 1) if p + 1 >= 10 else "0" + str(p + 1)
    return day

def month_h(h, l, m):
    return "0" + str((h + l - 7 * m + 114) // 31)

def easter_MJB(year):
    a = a_h(year)
    b = b_h(year)
    c = c_h(year)
    d = d_h(b)
    e = e_h(b)
    f = f_h(b)
    g = g_h(b, f)
    h = h_h(a, b, d, g)
    i = i_h(c)
    k = k_h(c)
    l = l_h(e, i, h, k)
    m = m_h(a, h, l)
    p = p_h(h, l, m)
    day = day_h(p)
    month = month_h(h, l, m)
    return day + "-" + month + "-" + str(year)


# 4. MAIN ALGORITHM
def easter_mjb_main(year):
    validate_input(year)

    result = easter_MJB(year)

    return result