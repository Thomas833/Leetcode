def isAlhpaNum(char: str) -> list:
    if (ord(char) >= 48 and ord(char) <= 57):
        return [True, char]
    elif ((ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90)):
        return [True, ord(char.lower())]
    else:
        return [False]

def palindrome(s: str) -> bool:
    i = 0
    j = len(s)-1
    
    while i < j:
        iChar = s[i]
        jChar = s[j]
        iAlpha = isAlhpaNum(iChar)
        jAlpha = isAlhpaNum(jChar)
        if iAlpha[0] and jAlpha[0]:
            if iAlpha[1] != jAlpha[1]:
                return False
            else:
                i+=1
                j-=1
        else:
            if not iAlpha[0]:
                i+=1
            if not jAlpha[0]:
                j-=1
    return True
print(palindrome(" "))