matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]

check if first row or first col have 0s. if they do, set boolean to true

iterate through matrix starting from index 1,1 to m,n. if the cell has a 0 in it, set
matrix[row][0] to 0 and matrix[0][col] to 0.

iterate through and change row to 0s if matrix[row][0] is 0
do the same for cols

lastly, check if the booleans are true. if so, change first row and/or first col to all zeros

return matrix

performance is n x m with O(1) space
