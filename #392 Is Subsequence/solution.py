def subsequence(s: str, t: str) -> bool:
    i = k = 0 # i is pointer for s, k is pointer for t
    while i < len(s) and k < len(t):
        if s[i] == t[k]:
            i+=1
        k+=1
    if i == len(s):
        return True
    return False
            


print(subsequence("abc", "andbc"))