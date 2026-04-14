def romanToInt(s: str) -> int:
    hashmap = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    arr = []
    num = 0
    for char in s:
        arr.append(char)
    for i in range(len(arr)):
        if i == len(arr)-1 or hashmap[arr[i]] >= hashmap[arr[i+1]]:
            num += hashmap[arr[i]]
        else :
            num -= hashmap[arr[i]]
    return num

print(romanToInt("MCMXCIV"))