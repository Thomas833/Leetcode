def solution(path: str)->str:
    output = []
    word = ""
    
    #append each dir to stack
    for i in range(1,len(path)):
        if path[i] != '/':
            word += path[i]
            if i + 1 == len(path):
                output.append(word)
        else:
            if len(word):
                output.append(word)
            word = ""
    stack = []
    #go through each dir and determine if valid. if so, append to output string
    for d in output:
        if d == ".." and stack:
            stack.pop()
        elif d != "." and d != "..":
            stack.append(d)
    
    output = ""
    for d in stack:
        output += "/" + d

    if not output:
        output = "/"
    return output

path ="/../"
print(solution(path))


# just split according to slashes
def efficientSolution(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()          
            elif part == "." or part == "":
                continue                 
            else:
                stack.append(part)      

        return "/" + "/".join(stack)     
        