def solution(board: list[list[int]]) -> list[list[int]]:
    rows = len(board)
    cols = len(board[0])

    # -1 means is currently alive(1) and will die(0)
    # 2 means is currently dead(0) and will come alive(1)

    # iterate through array and update cell according to neighbors
    for i in range(rows):
        for j in range(cols):
            # if alive and less than 2 or more than 3, die. 
            # if dead and 3, become alive
            status = 0

            top = True if i-1>=0 else False
            bottom = True if i+1<rows else False
            right = True if j+1<cols else False
            left = True if j-1>=0 else False

            #first check cardinal directions
            #check top neighbor
            if top and (board[i-1][j] == 1 or board[i-1][j] == -1): # if neighbor is currently 1
                status += 1

            #check bottom neighbor
            if bottom and (board[i+1][j] == 1 or board[i+1][j] == -1):
                status += 1
            
            #check right and possible diag right neighbor
            if right and (board[i][j+1] == 1 or board[i][j+1] == -1):
                status += 1

            #check left neighbor
            if left and (board[i][j-1] == 1 or board[i][j-1] == -1):
                status += 1
            
            #check diagonal directions
            #check top right neighbor
            if top and right and (board[i-1][j+1] == 1 or board[i-1][j+1] == -1):
                status += 1

            #check top left neighbor
            if top and left and (board[i-1][j-1] == 1 or board[i-1][j-1] == -1):
                status += 1

            #check bottom right neighbor
            if bottom and right and (board[i+1][j+1] == 1 or board[i+1][j+1] == -1):
                status += 1
            
            #check bottom left neighbor
            if bottom and left and (board[i+1][j-1] == 1 or board[i+1][j-1] == -1):
                status += 1

            #check status and state of current cell (alive or dead) and decide if transformation is needed
            if board[i][j] == 0:
                if status == 3:
                    board[i][j] = 2 # dead and will come alive
            else:
                if status > 3 or status < 2:
                    board[i][j] = -1 # alive but will die

    #update board according to value
    for i in range(rows):
        for j in range(cols):
            if board[i][j] > 1:
                board[i][j] = 1
            elif board[i][j] < 0:
                board[i][j] = 0
    return board



board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# for row in solution(board):
#     print(row)
board = solution(board)