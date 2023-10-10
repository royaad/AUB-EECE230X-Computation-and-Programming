# Helper function
def MaxDiameter(s, i, j):
    if i == j:
        start = end = i
        n = len(s) - 1
        while start > 0 and end < n and s[start-1] == s[end+1]:
            start -= 1
            end += 1
        return end - start + 1
    else:
        n = len(s) - 1
        if i < n:
            if s[i] == s[j]:
                start = i
                end = j
                while start > 0 and end < n and s[start-1] == s[end+1]:
                    start -= 1
                    end += 1
                return end - start + 1     
            else:
                return 1
        else:
            return 1     

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
            diam = MaxDiameter(s, i, i)
            if diam > old_diam:
                old_diam = diam
                start = i - diam//2
                end = i + diam//2
            # Even length palindromes such as "abba" have 2 centers of indices "1" and "2"
            diam = MaxDiameter(s, i, i + 1)
            if diam > old_diam:
                old_diam = diam
                start = i + 1 - diam//2
                end = i + diam//2
        return s[start:end+1]
    else:
        return ""

input_word = "ccbbabbc"
print(longestPalSubsC(input_word))