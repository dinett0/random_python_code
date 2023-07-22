def to_rpn(expression):
    def preced(op):
        lookup = {"~": 0, "->": 1, "^": 2, "or": 3, "and": 4, "not": 5, "(": -1}
        return lookup[op]

    ans = []
    operators = []
    for token in expression.replace("(", "( ").replace(")", " )").split():
        if token in "ABC":
            ans.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                ans.append(operators.pop())
            operators.pop()
        else:
            while operators and (
                preced(operators[-1]) > preced(token)
                or preced(operators[-1]) == preced(token)
            ):
                ans.append(operators.pop())
            operators.append(token)

    for operator in operators[::-1]:
        ans.append(operator)

    return ans
