We must check each of the three rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

To check that each row and column are valid, we will put the row data and col data into dedicated hashmaps

The key will be the row/col and the values will show all the values found in said row/col.

To check what box we are in, we will use floor division on the row index and col index with 3. 
    for the square at (4,5), it's in box 4//3=1, 5//3=1 (1,1)
    at (5,8), we are in box (1,2)
    This means boxes range from (0,0) to (0,2) to (2,0) to (2,2)
Similarly, we will use a hashmap to store the tuple of the box as the key and will store the values in said box as values in a set.

I will use nested for loops to iterate through the matrix and perform these calculations. If I ever find a duplicate, I will return false. 