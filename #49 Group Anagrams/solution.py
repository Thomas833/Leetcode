def solution(strs: list[str])->list[list[str]]:
    hashmap = {}
    output = []

    for s in strs:
        sSorted = ''.join(sorted(s))
        if sSorted not in hashmap:
            hashmap[sSorted] = len(output)
            output.append([s])
        else:
            output[hashmap[sSorted]].append(s)
    return output

print(solution(["eat","tea","tan","ate","nat","bat"]))
