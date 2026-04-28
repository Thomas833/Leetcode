def spiralOrder(matrix: list[list[int]]) -> list:
    left = 0
    right = len(matrix[0])-1
    bottom = len(matrix)-1
    top = 0
    output = []
    while left <= right and top <= bottom:
         # left → right
        for j in range(left, right + 1):
            output.append(matrix[top][j])
        top += 1

        # top → bottom
        for i in range(top, bottom + 1):
            output.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # right → left
            for j in range(right, left - 1, -1):
                output.append(matrix[bottom][j])
            bottom -= 1

        if left <= right:
            # bottom → top
            for i in range(bottom, top - 1, -1):
                output.append(matrix[i][left])
            left += 1
    return output


matrix = [ [1,2,3]
          ,[4,5,6]
          ,[7,8,9]]
print(spiralOrder(matrix))