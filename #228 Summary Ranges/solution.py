def solution(nums: list[int])->list:
    def outputStr(l,r)->str:
        if l == r:
            return str(l)
        else:
            return str(l)+"->"+str(r)
        
    l = 0
    output = []

    for r in range(len(nums)):
        if r+1==len(nums) or nums[r+1] != nums[r]+1:
            output.append(outputStr(nums[l],nums[r]))
            l = r+1
    return output
    

nums = [0,1,2,4,5,7]
print(solution(nums))
