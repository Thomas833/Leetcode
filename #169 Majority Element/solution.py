def mySolution(nums: list[int]) -> int:
    val = nums[0]
    votes = 0

    for i in range(len(nums)):
        if votes == 0:
            val = nums[i]
            votes += 1 
        else:
            if nums[i] == val:
                votes += 1
            else:
                votes -= 1
    return val

            

    
print(mySolution([1,2,3,1,5,6,7,1,1]))