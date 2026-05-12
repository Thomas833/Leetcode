def solution(s: str)->bool:
    pmap:dict[str:str] = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    for i in range(len(s)):
        if s[i] not in pmap:
            stack.append(s[i])
        elif stack and stack[-1] == pmap[s[i]]:
            stack.pop()
        else:
            return False
    if not stack:
        return True
    else:
        return False

s = "()[]{}" # stack = ([
print(solution(s))
