def solution(nums: list[int])->int:    
    numSet = set(nums)
    maxCount = 0

    for n in numSet:
        if n-1 not in numSet: 
            length = 1
            while n+length in numSet:
                length+=1
            maxCount = max(length,maxCount)
    return maxCount

nums = [100,4,200,1,3,2]
print(solution(nums))
