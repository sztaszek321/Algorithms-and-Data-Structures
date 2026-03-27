# 1. IMPORTS & SAMPLES/TESTCASES

data_sample = [
    "kajak",
    "anna",
    "radar",
    "level",
    "1221",
    "12321",
    "dom",
    "python",
    "12345",
    "kajaki",
    "abcd",
    "a",
    "",
    "aa",
    "ab",
    "Kobyła ma mały bok",
    "A man, a plan, a canal: Panama!",
    "No lemon, no melon",
    "abacaba",
    "banana",
    "racecarxyz",
    "abcddcbaxyz"
]

# 2. DATA VALIDATION
def validate_input(text):
    if text is None:
        raise ValueError("Input cannot be None")
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    return text.lower()


# 3. HELPER FUNCTIONS
def palindrome(text):
    n = len(text)
    l = n // 2
    if n % 2 == 1:
        h = l+1
    else:
        h = l
    first = text[:l]
    second = text[h::]
    second = second[::-1]

    print(first, second)

    if first == second:
        return True
    return False

def manacher(text):
    n = len(text)
    t = "/" + text + "/"
    arr =[[]]
    f = True

    for j in range(2):
        arr[j][0] = 0
        i = 1
        r = 0
        while i <= n:
            while t[i-r-1] == t[i+j+r]:
                r += 1
            arr[j][i] = r
            k = 1
            while f:
                if arr[j][i-k] == r - k:
                    f = False
                elif k >= r:
                    f = False
                else:
                    arr[j][i+k] = min(arr[j][i-k], r-k)
                    k += 1
            f = True
            r = max(r-k, 0)
            i = i+k
        t = text[1:n]
        for i in range(n):
            for j in range(2):
                a = arr[j][i]
                while a >= 1:
                    print(t[i-r-1:i+2*r+j])
                    a -= 1



# 4. MAIN ALGORITHM
def palindrome_main(sample):
    sample = validate_input(sample)

    result = palindrome(sample)
    manacher(sample)

    return result


print(palindrome_main(data_sample[1]))