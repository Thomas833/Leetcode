def solution(intervals: list[list[int]], newInterval: list[int])->list[list[int]]:
    output = []

    for interval in intervals: # merging or in middle
        #current interval entirely before newInterval
        if interval[1] < newInterval[0]:
            output.append(interval)

        #newInterval completely after interval
        elif interval[0] > newInterval[1]:
            output.append(newInterval)
            newInterval = interval    

        #overlap
        else:
            newInterval[0] = min(interval[0], newInterval[0])
            newInterval[1] = max(interval[1], newInterval[1])
    output.append(newInterval)
    return output


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(solution(intervals, newInterval))
