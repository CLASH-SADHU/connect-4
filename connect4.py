
board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
ROW_COUNT = 8
COLUMN_COUNT = 6
PIECE_ONE = "X"
PIECE_TWO = "O"
def draw_field(field):
    for row in range(11):
        if row%2 == 0:
            playing_row = int(row/2)
            for column in range(13):
                if column%2 == 0:
                    playing_column = int(column/2)
                    if column != 12:
                        print(field[playing_column][playing_row],end="")
                    else :
                        print(field[playing_column][playing_row])
                else:
                    print("|",end="")   
        else:
            print("-------------")

# copiedBoard = list(reversed(board)) 
# print(copiedBoard) 
""" def print_board(board):
    inverted_board = list(reversed(board))
    draw_field(inverted_board) """
def update_board(col, player):
    column = board[col]
    index = ""
    reversed_column = column[::-1]
    for row in reversed_column:
        if row == " ":
            index = reversed_column.index(row)
            reversed_column[index] = "X" if player == 1 else "O"
            break
    if index == "":
        return False
    column = reversed_column[::-1]
    board[col] = column
    draw_field(board)
    return True
       
def is_valid_location(col):
    if col >=1 and col<=7:
        return True
    else:
        return False
""" def get_open_row (board,col):
    for r in range(ROW_COUNT-1):
        if board[r][col] == " ":
            return r """ 
draw_field(board)
game_over = False
player = 1
while not game_over:
    if player == 1 :
        col = int(input("Player 1, enter a digit from 0-6: \n"))
        if is_valid_location(col) == False:
            print('invalid move')
        else:
            # get_open_row(board,col)
            update_board(col-1,player)
            player = 2
            draw_field(board)
    
            

    else:
        col = int(input("Player 2, enter a digit from 0-6: \n")) 
        if is_valid_location(col) == False:
            print('invalid move')
        else:
            # get_open_row(board,col)
            update_board(col-1,player)
            player = 1
            draw_field(board)
    



  








 