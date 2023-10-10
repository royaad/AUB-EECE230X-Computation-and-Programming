def count(s, n):
    D = {}
    for i in range(n):
        if s[i] not in D:
            D[s[i]] = 1
        else:
            D[s[i]] += 1
    return D

def anagrams(s1, s2):
    # If the length is not the same then it is not an anagram
    n1 = len(s1)
    n2 = len(s2)
    if n1 != n2: return False
    
    # If the length is the same
    # Create a dictionary of the letters and count in each word
    D1 = count(s1, n1)
    D2 = count(s2, n2)
    return D1 == D2

print(anagrams("",""))
print(anagrams("i","i"))
print(anagrams("is","si"))
print(anagrams("fun","nfu"))
print(anagrams("aaabaab","abba"))
print(anagrams("aaabaab","baabaaa"))
print(anagrams("EECE230","EECE230"))
print(anagrams("EECE230","3EE02CE"))
print(anagrams("EECE230","3EEE02E"))