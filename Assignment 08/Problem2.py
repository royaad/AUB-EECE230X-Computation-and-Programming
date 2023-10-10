def isPalindrome(s): # Wrapper function
    def isPalindromeRec(s, low, high):
        '''
        Recursive function which checks if substring s[low ... high] is palindrome
        returns a True/False value
        '''
        if low > high:
            return True
        if s[low] != s[high]:
            return False
        else:
            if high-low <= 1:
                return True
            else:
                return isPalindromeRec(s, low+1, high-1)

    n = len(s)
    return isPalindromeRec(s,0,n-1)

print(isPalindrome("anna"))
print(isPalindrome("civic"))
print(isPalindrome("a"))
print(isPalindrome("tx1aa1xt"))
print(isPalindrome(""))
print(isPalindrome("Civic"))
print(isPalindrome("ab"))