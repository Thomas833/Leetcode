def solution(nums: list, val: int)->list:
    j = len(nums)-1
    i = 0
    k = 0
    while i<=j:
        if nums[j] == val:
            j-=1
            continue
        if nums[i] == val:
            t = nums[j]
            nums[j] = nums[i]
            nums[i] = t
            i+=1
            k+=1
        else:
            k+=1
            i+=1
    #print(arr)
    return k

print(solution([0,1,2,2,3,0,4,2], 2))     
