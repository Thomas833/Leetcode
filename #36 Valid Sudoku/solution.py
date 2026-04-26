from collections import defaultdict
def validSudoku(board: list[list[str]]) -> bool:
    colMap = defaultdict(set)
    rowMap = defaultdict(set)
    boxMap = defaultdict(set)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == ".":
                continue
            if val in rowMap[r] or val in colMap[c] or val in boxMap[(r//3,c//3)]:
                return False
            
            rowMap[r].add(val)
            colMap[c].add(val)
            boxMap[(r//3,c//3)].add(val)

    return True



board = [["5","3",".",".","7",".",".",".","."]
        ,["2",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(validSudoku(board))