def rotateImage(matrix: list[list[int]])-> list[list[int]]:
    matrix.reverse()
    print(matrix)
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

beg = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
end = rotateImage([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
for i in range(len(beg)):
    print(str(beg[i]) + "   " + str(end[i]))