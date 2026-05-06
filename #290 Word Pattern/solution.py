def solution(pattern: str, s: str)->bool:
    pmap = {}
    smap = {}
    sLen = 1
    pLen = len(pattern)

    # get length of s
    for c in s:
        if c == " ":
            sLen += 1

    # compare lengths
    if sLen != pLen:
        return False
    
    # populate hashmap and iterate through pattern and 
    i = 0
    j = 0
    k = 0 # iterate through pattern
    while j < len(s):
        word=""
        if j + 1 == len(s):
            word = s[i:j+1]
        elif s[j] == " ":
            word = s[i:j]
        else:
            j+=1
            continue
        if word not in smap and pattern[k] not in pmap:
            smap[word] = pattern[k]
            pmap[pattern[k]] = word
            k+=1
            i=j+1
        elif (word in smap and pattern[k] in pmap and word != pmap[pattern[k]]) or (word not in smap and pattern[k] in pmap) or (pattern[k] not in pmap and word in smap):
            return False
        else:
            i=j+1
            k+=1
        j+=1
    return True

print(solution("aba", "dog cat dog"))
