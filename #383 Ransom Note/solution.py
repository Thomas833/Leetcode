def solution(magazine: str, ransomNote: str)->bool:
    hashmap = {}

    # go through magazine and populate 
    for c in magazine:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            hashmap[c] += 1

    # go through ransomNote and check against hashmap.
    for c in ransomNote:
        if c in hashmap and hashmap[c] > 0:
            hashmap[c] -= 1
        else:
            return False
    return True


magazine = "aba"
ransomNote = "aab"
print(solution(magazine, ransomNote))
