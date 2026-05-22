class Solution:
    def calculate(self, s: str) -> int:
        def update(op, val):
            match op:
                case "+":
                    stack.append(val)
                case "-":
                    stack.append(-val)
                case "/":
                    stack.append(int(stack.pop() / val))
                case "*":
                    stack.append(stack.pop() * val)

        i, sign, stack, num = 0,"+",[],0
        
        while i < len(s):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] in "*+-/":
                update(sign, num)
                sign, num = s[i], 0
            elif s[i] == "(":
                j, num = self.calculate(s[i+1:])
                i += j
            elif s[i] == ")":
                update(sign, num)
                return i+1, sum(stack)
            i += 1
        update(sign, num)
        return sum(stack)
    


def main():
    sol = Solution()
    s = "(1+(4+5+2)-3)+(6+8)"
    print(sol.calculate(s))
main()