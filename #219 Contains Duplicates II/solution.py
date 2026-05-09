def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    i = 0
    j = 1
    hashmap = {}
    #handle small inputs
    if len(nums) == 1 or k == 0:
        return False
    hashmap[nums[i]] = i
    #iterate through list
    while j < len(nums):
        # i-j < k
        if abs(i-j) < k:
            if nums[j] in hashmap: # we have matching val in the range
                return True
            else:
                hashmap[nums[j]] = j
                j+=1
        else: #i-j = k
            if nums[j] in hashmap:
                return True
            else:
                hashmap.pop(nums[i])
                i+=1
                hashmap[nums[j]] = j
                j+=1
    return False


nums = [4,1,2,3,1,5]
k = 3
print(containsNearbyDuplicate(nums,k))
