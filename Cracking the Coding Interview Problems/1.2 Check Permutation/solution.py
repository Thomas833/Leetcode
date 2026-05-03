def hashmap(s1: str, s2: str)->bool:
    hashmap = {}
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[i] not in hashmap:
                hashmap[s1[i]] = [1,0]
            else:
                hashmap[s1[i]][0] += 1
            if s2[i] not in hashmap:
                hashmap[s2[i]] = [0,1]
            else:
                hashmap[s2[i]][1] += 1

        for key in hashmap:
            v0 = hashmap[key][0]
            v1 = hashmap[key][1]
            if v1 != v0:
                return False
        return True
    else:
        return False


s1 = "abs"
s2 = "sca"

print(hashmap(s1,s2))