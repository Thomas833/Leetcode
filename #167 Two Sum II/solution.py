def twoSum(numbers: list, target: int) -> list[int]:
    i = 0
    j = len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] > target:
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            return [i+1, j+1]


print(twoSum([2,3,4], 6))