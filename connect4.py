board = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]]
COLUMN_COUNT = 7
ROW_COUNT = 6
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
def update_board(col, player):
    column = board[col]
    index = ""
    invert_col = column[::-1]
    for row in invert_col:
        if row == " ":
            index = invert_col.index(row)
            invert_col[index] = "X" if player == 1 else "O"
            break
    if index == "":
        print("The column is full , try different column:")
        main()
    column = invert_col[::-1]
    board[col] = column
    draw_field(board)
    return True       
def is_valid_location(col):
    if col >=1 and col<=7:
        return True
    else:
        return False
def check_winner(board,player):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-2):
		for r in range(ROW_COUNT):
			if board[c+1][r] == player and board[c+2][r] == player and board[c+3][r] == player and board[c+4][r] == player:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[c][r] == player and board[c][r+1] == player and board[c][r+2] == player and board[c][r-1] == player:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
				return True
def main():
    draw_field(board)
    game_over = False
    player = 1
    turn = 0
    while not game_over:
        if player == 1 :
            col = int(input("Player 1, enter a digit from 1-7: \n"))
            if is_valid_location(col) == False:
                print('invalid move')
            else:
                # get_open_row(board,col)
                update_board(col-1,player)
                player = 2   
                winner = check_winner(board,player=2)
                if winner == True:
                    print(player,"wins")
                    game_over = True 
        else:
            col = int(input("Player 2, enter a digit from 1-7: \n")) 
            if is_valid_location(col) == False:
                print('invalid move')
            else:
                update_board(col-1,player)
                player = 1
                winner = check_winner(board,player=2)
                if winner == True:
                    print(player,"wins")
                    game_over = True             
        turn +=1
    draw_field(board)
main()
    



  








 