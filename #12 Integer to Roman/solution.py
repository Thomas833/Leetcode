def intToRoman(num: int) -> str:
    mod = 0
    hashmap = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M" 
    }

    romanStr = ""
    while mod != 1:
        numLen = len(str(num))
        mod = 10**(numLen-1)
        suffixNum = num % mod
        romanNum = num - suffixNum
        reducedNum = int((num - suffixNum) / mod)
        if reducedNum == 4 or reducedNum == 9:
            romanStr += hashmap[mod] + hashmap[romanNum+(romanNum/reducedNum)]
        elif reducedNum < 4 and reducedNum != 0:
            romanStr += reducedNum*(hashmap[romanNum/reducedNum])
        elif reducedNum > 4:
            diff = reducedNum - 5
            romanStr += hashmap[5*mod] + diff*(hashmap[romanNum/reducedNum])
        num = suffixNum
    return romanStr

num = 1994 
print(intToRoman(num))
print("MCMXCIV")