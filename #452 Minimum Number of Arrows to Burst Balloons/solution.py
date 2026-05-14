def solution(points: list[list[int]])->bool:
    count = 1
    points.sort()
    end = points[0][1]
    for point in points[1:]:
        #no overlap
        if point[0] > end:
            count+=1
            end = point[1]
        else: #overlap exists
            end = min(end,point[1])
    return count

points = [[1,2],[2,3],[3,4],[4,5]]
print(solution(points))

def efficientSolution(points: list[list[int]])->bool:
    points.sort(key=lambda x:x[1])
    arrows = 1
    last_end = points[0][1]

    for start, end in points:
        if start>last_end:
            arrows += 1
            last_end = end
    return arrows
