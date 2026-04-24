def minSubArr(nums: list, target: int) -> int:
    minLength = len(nums)+1
    j = 0
    i = 0
    val = "j"
    s = 0
  

    while i <= j and j < len(nums):
        if val == "j":
            s += nums[j]
        else:
            s -= nums[i]
            i+=1
        if i == j and s >= target:
            return 1
        if s >= target:
            if j-i+1 < minLength:
                minLength = j-i+1
            val = "i"
        else: 
            j += 1
            val = "j"

    if minLength < len(nums)+1:
        return minLength
    return 0

print(minSubArr([1,2,3,4,5], 15))