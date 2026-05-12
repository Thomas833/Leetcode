def solution(intervals: list[list[int]])->list[list[int]]:
    output = []
    intervals.sort()
    prev = intervals[0]
    for i in range(1,len(intervals)):
        cl = intervals[i][0]
        cr = intervals[i][1]
        pr = prev[1]
        if cl <= pr:
            prev[1] = max(cr,pr)
        else:
            output.append(prev)
            prev = intervals[i]
    output.append(prev)
    return output
            

x = [[1,3],[2,6],[8,10],[15,18]]
print(solution(x))
