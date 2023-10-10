# def longestPalSubsA(s):
#     n = len(s)
#     for i in range(n-1):
#         for j in range(i+1):
#             t = s[j:j+n-i]
#             if t == t[::-1]:
#                 print(t)

def longestPalSubsA(s):
    if len(s):
        start = end = 0
        n = len(s)
        output = s[0]
        for i in range(n):
            for j in range(i, n):
                t = s[i:j+1]
                if t == t[::-1] and (j-i+1) > (end-start+1):
                    start = i
                    end = j
                    output = t
        return output
    else:
        return ""

# Read and convert the first input sequence
# input_word = input("Enter a word: ")
input_word = "abba123"
print(longestPalSubsA(input_word))
