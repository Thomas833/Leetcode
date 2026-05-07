def solution(s:str, t:str)->bool:
    if len(s) != len(t):
        return False
    
    smap = {}
    tmap = {}

    # fill out smap with characters and respective counts from s
    for c in s:
        if c not in smap:
            smap[c] = 1
        else:
            smap[c] += 1
    
    # fill out tmap and check if each letter in t is in smap
    for c in t:
        if (c not in smap) or (c in tmap and c in smap and tmap[c] >= smap[c]):
            return False
        else:
            if c not in tmap:
                tmap[c] = 1
            else:
                tmap[c] += 1
    
    # compare tmap and smap
    for c in t:
        if tmap[c] != smap[c]:
            return False
    return True


print(solution("anagram", "nagarbam"))




def optimalSolutionFromLeetCode( s: str, t: str) -> bool:
        if len(s) != len(t):

            return False
        for i in set(s):

            if s.count(i) != t.count(i):
                return False
        return True
# reduce s to unique characters and compare the counts in s and t. no need to check same character multiple times