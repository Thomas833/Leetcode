def solution(s: str, t: str) -> bool:
    smap = {}
    tmap = {}
    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]
        if c1 not in smap:
            smap[c1] = c2
        else:
            if smap[c1] != c2:
                return False
        if c2 not in tmap:
            tmap[c2] = c1
        else:
            if tmap[c2] != c1:
                return False
    return True



s = "f11"
t = "b23"
print(solution(s,t))
