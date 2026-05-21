def evalRPN(tokens: list[str]) -> int:
    stack = []
    operands = {
        "+": 1,
        "-": 1,
        "*": 1,
        "/": 1
    }
    for t in tokens:
        if t not in operands:
            stack.append(int(t))
        else:
            r = stack.pop()
            l = stack.pop()
            stack.append(computation(l,r,t))
    return stack[0]


def computation(l: int, r: int, o: str) -> int:
    match o:
        case "+":
            return l + r
        case "-":
            return l - r
        case "*":
            return l * r
        case "/":
            return int(l / r)

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))



# this one is just slightly more efficient and i liked the tricks they used
def efficientSolution(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c in "+-*/":
                a = int(stack.pop())
                b = int(stack.pop())
                if c == "+":
                    ans = a + b
                if c == "-":
                    ans = b - a
                if c == "*":
                    ans = a * b
                if c == "/":
                    ans = b / a
                stack.append(ans)
            else:
                stack.append(c)

        return int(stack.pop())