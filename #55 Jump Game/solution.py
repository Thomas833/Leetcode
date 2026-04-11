def jump(nums: list[int]) -> bool:
    jumps = 0
    if len(nums) == 1:
        return True
    for i in range(len(nums)):
        if nums[i] > jumps:
            if nums[i] + i >= len(nums) - 1:
                return True
            jumps = nums[i]
        elif jumps == 0 and nums[i] == 0:
            break
        jumps -=1 
    return False
            

print(jump([3,2,0,4,0,0,0,0]))