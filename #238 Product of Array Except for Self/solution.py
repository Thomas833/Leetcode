def solution(nums: list[int]) -> list[int]:
    out = []
    prefix = 1
    for i in range(len(nums)):
        out.append(prefix)
        prefix = prefix * nums[i]
    prefix = 1
    for i in range(len(nums)-1, -1, -1):
        out[i] = out[i] * prefix
        prefix = prefix*nums[i]
    return out

print(solution([1,2,3,4]))