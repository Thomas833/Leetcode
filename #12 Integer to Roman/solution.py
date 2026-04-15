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
        romanStr += hashmap[romanNum]

        
        

print(intToRoman(2345))