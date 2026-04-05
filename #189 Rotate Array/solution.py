def mySolution(nums, k) -> None: # looked at solution a bit to get ideas. 
    k %= len(nums)

    def reverse(left, right):
        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
    
    reverse(0, len(nums)-1)
    reverse(0, k-1)
    reverse(k, len(nums)-1)


mySolution([1,2,3,4,5,6,7], 2)