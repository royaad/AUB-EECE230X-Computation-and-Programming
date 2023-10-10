def parenthesesAndBracesChecker(s):
    n = len(s)
    temp = []
    for i in range(n):
        if s[i] == "(" or s[i] == "[":
            temp.append(s[i])
        elif s[i] == ")":
            if len(temp) == 0 or temp.pop() != "(":
                return False
        elif s[i] == "]":
            if len(temp) == 0 or temp.pop() != "[":
                return False
    return True if len(temp) == 0 else False

s = "a(aa)aa"
print(parenthesesAndBracesChecker(s))
s = "([aa(b)c[[aaaaa]]r(d)])"
print(parenthesesAndBracesChecker(s))
s = "aa(b(cd))e[ab]"
print(parenthesesAndBracesChecker(s))
s = "aa(b(cd)"
print(parenthesesAndBracesChecker(s))
s = "a([b)]"
print(parenthesesAndBracesChecker(s))
s = "((aab)d"
print(parenthesesAndBracesChecker(s))
s = "(("
print(parenthesesAndBracesChecker(s))
s = "ef)]"
print(parenthesesAndBracesChecker(s))
