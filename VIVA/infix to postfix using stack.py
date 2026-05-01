def infix_to_postfix(exp):
    stack = []
    res = ""
    p = {'+':1, '-':1, '*':2, '/':2, '^':3}

    for ch in exp:
        if ch.isalnum():
            res += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != '(' and p[ch] <= p[stack[-1]]:
                res += stack.pop()
            stack.append(ch)

    while stack:
        res += stack.pop()
    return res

print(infix_to_postfix("A+B*(C-D)"))