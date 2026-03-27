# 1. IMPORTS & SAMPLES/TESTCASES

sample_data = [1900, 2000, 2004, 2025]

# 2. DATA VALIDATION
def validate_input(year):
    if year is None:
        raise ValueError("Input cannot be None")


# 3. HELPER FUNCTIONS
def helper_function(year):
    return year


# 4. MAIN ALGORITHM
def algorithm_name(year):
    validate_input(year)

    result = helper_function(year)

    return result