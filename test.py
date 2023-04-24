
# Each cell can be 'X', 'O', or ' '
board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def gameOver(board):
    for row in board:
        if row[0]!=' ' and row[1]==row[0] and row[1]==row[2]:
            return True
    for col in range(3):
        if board[0][col]!=' ' and board[0][col]== board[1][col] and board[1][col] ==board[2][col]:
            return True
    if board[0][0] != ' ' and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return True
    if board[0][2] != ' ' and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return True
    return False

gameOver(print(board))
    
        
    


    


        