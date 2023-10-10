# Helper function
def MaxDiameter(s, i, j):
    # I initiate start, end, and n
    start = i
    end = j
    n = len(s)
    # Instead of checking multiple if else cases all checks are performed in the condition of the while loop
    while start >= 0 and end < n and s[start] == s[end]:
        start -= 1
        end += 1
    # The while will teminate 1 condition too late so we need to revert the end by -1 and the start by +1
    # The true diameter is thus (end - 1) - (start + 1) + 1 = end - start - 1
    # I will make the function return start and end to simplify calculations also
    return start + 1, end - 1, end - start - 1

def longestPalSubsC(s):
    if len(s):
        start = end = 0
        old_diam = end - start + 1
        n = len(s)
        # Looping over centers
        for i in range(n):
            # We have 2 cases
            # We will use a helper function to get the longest sub palindrome for each center
            # Odd length palindromes such as "aba" have 1 center index "1"
            start_, end_, diam = MaxDiameter(s, i, i)
            if diam > old_diam:
                old_diam = diam
                start = start_
                end = end_
            # Even length palindromes such as "abba" have 2 centers of indices "1" and "2"
            start_, end_, diam = MaxDiameter(s, i, i + 1)
            if diam > old_diam:
                old_diam = diam
                start = start_
                end = end_
        return s[start:end+1]
    else:
        return ""

input_word = "ccbbabbc"
print(longestPalSubsC(input_word))