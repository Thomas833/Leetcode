def hashmap(string: str) -> bool:
    hashmap = {}
    for c in string:
        if c not in hashmap:
            hashmap[c] = 1
        else:
            return False
    return True

def bitVector(string: list[str]) -> bool:
    bit_vector = 0
    for c in string:
        pos = ord(c.lower()) - 97 #assuming lowercase a-z only
        if bit_vector & (1<<pos):
            return False
        else:
            bit_vector |= (1<<pos) #set the value at index pos to 1
    return True


inStr = "thsomas"
print(hashmap(inStr))
print(bitVector(inStr))
