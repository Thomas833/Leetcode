def threeSome(nums: list[int]) -> list[list[int]]:
    output = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
                continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                output.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j] == nums[j-1] and j < k:
                    j += 1
    return output

# [-4,-1,-1,0,1,1,2]
print(threeSome([-4,-1,-1,0,1,1,2]))