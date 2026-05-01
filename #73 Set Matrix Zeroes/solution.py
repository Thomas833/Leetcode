def solution(matrix):
    first_row_has_0 = False
    first_col_has_0 = False
    rows = len(matrix)
    cols = len(matrix[0])

    # check if first row has 0s
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_has_0 = True
            break
    
    # check if first col has 0s
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_has_0 = True
            break

    # walk through matrix and set row/col to 0 if val is 0
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    # set rows to 0 if matrix[row][0] is 0
    for i in range(1,rows):
        if matrix[i][0] == 0:
            for j in range(cols):
                matrix[i][j] = 0

    # set cols to 0 if  matrix[0][col] is 0
    for j in range(1,cols):
        if matrix[0][j] == 0:
            for i in range(rows):
                matrix[i][j] = 0
    
    # if first row has 0, set row to 0s
    if first_row_has_0:
        for j in range(cols):
            matrix[0][j] = 0
    
    # if first col has 0s in it, set all to 0s
    if first_col_has_0:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix




matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(solution(matrix))
