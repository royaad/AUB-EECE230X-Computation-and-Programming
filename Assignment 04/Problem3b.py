def isSubsequencePalindrome(s, start, end):

    # Initiate state
    isPalindrome = True
    n = end - start + 1

    for i in range(n//2):
        if s[start+i] != s[end-i]:
            isPalindrome = False
            return isPalindrome
    
    return isPalindrome

def longestPalSubsB(s):
    if len(s):
        start = end = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                if isSubsequencePalindrome(s, i, j) and (j-i+1) > (end-start+1):
                    start = i
                    end = j
        return s[start:end+1]
    else:
        return ""

# print(isSubsequencePalindrome("123abba", 0, 2))
# print(isSubsequencePalindrome("123abba", 3, 6))

input_word = "1221"
print(longestPalSubsB(input_word))