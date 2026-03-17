# 1. IMPORTS & SAMPLES/TESTCASES

sample_data = [1582, 1600, 1700, 1800, 1900, 1996, 2000, 2001, 2004, 2024, 2025, 2026, 2100, 2400, 2040, 2056]

# 2. DATA VALIDATION
def validate_input(year):
    if year is None:
        raise ValueError("Input cannot be None")
    if not isinstance(year, int):
        raise ValueError("Input must be int")

    return year


# 3. HELPER FUNCTIONS
def is_leap(year):
    if year % 400 == 0:
        return True

    if year % 4 == 0:
        if year % 100 != 0:
            return True

    return False


# 4. MAIN ALGORITHM
def leap_year_main(year):
    year = validate_input(year)

    result = is_leap(year)

    return result