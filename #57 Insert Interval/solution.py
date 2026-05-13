def solution(intervals: list[list[int]], newInterval: list[int])->list[list[int]]:
    output = []
    status = "pre"
    curInt = newInterval

    if len(intervals) == 0:
        return [newInterval]
    if newInterval[0] > intervals[-1][1]: # larger than intervals
        output.append(intervals)
        output.append(newInterval)
        return output
    if newInterval[0] < intervals[0][0] and newInterval[1] < intervals[0][1]: # smaller than intervals
        output.append(newInterval)
        output.append(intervals)
        return output

    for i in range(len(intervals)): # merging or in middle
        if newInterval[1] < intervals[i][0]:

    return output


intervals = [[1,5]]
newInterval = [0,3]
print(solution(intervals, newInterval))
