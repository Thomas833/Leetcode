def longestCommonPrefix(strs):
    if (len(strs) == 1):
        return strs[0]
    if len(strs) == 0:
        return ""
    index = 1
    lcp = ""
    strs.sort()
    while index <= len(strs[0]):
        temp = strs[0][:index]
        if temp != strs[len(strs)-1][:index]:
            return lcp
        else:
            lcp = temp
        #print("index: " + str(index) + " | lcp: " + str(lcp))
        index +=1
    return lcp
    


strs = ["flower", "florist", "flight"]
print(longestCommonPrefix(strs))
