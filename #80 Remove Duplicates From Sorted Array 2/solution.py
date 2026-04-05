def mySolution(nums: list[int]) -> int:
    i = j = 0
    hashmap = {}
    while j < len(nums):
        if nums[j] not in hashmap:
            hashmap[nums[j]] = 1
            nums[i] = nums[j]
            i += 1
        elif hashmap[nums[j]] < 2:
            hashmap[nums[j]] += 1
            nums[i] = nums[j]
            i += 1
        j += 1
    print(nums)
    return i  

def efficientSolution(nums):
        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1 

        return k       

print(mySolution([1,1,1,2,2,3]))