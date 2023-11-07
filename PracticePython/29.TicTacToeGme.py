def drawboard(board):
    print (str(board[0][0])+' '+str(board[0][1])+' '+str(board[0][2]) )
    print (str(board[1][0])+' '+str(board[1][1])+' '+str(board[1][2]) )
    print (str(board[2][0])+' '+str(board[2][1])+' '+str(board[2][2]) )

game = [[".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]]

while True:
    while True:
        drawboard(game)
        cords = input("Where do you want to put X? ")
        cords = cords.replace(',','')
        cords = list(cords)
        row = cords[0]
        col = cords[1]
        if game[int(row)-1][int(col)-1] != '.':
            print("This spot is taken.")
        else:
            game[int(row)-1][int(col)-1] = 'X'
            break
    while True:
        drawboard(game)
        cords = input("Where do you want to put O? ")
        cords = cords.replace(',', '')
        cords = list(cords)
        row = cords[0]
        col = cords[1]
        if game[int(row)-1][int(col)-1] != '.':
            print("This spot is taken.")
        else:
            game[int(row) - 1][int(col) - 1] = 'O'
            break

def check(board):
	for x in range(0,3):
		row = set([board[x][0],board[x][1],board[x][2]])
		if len(row) == 1 and board[x][0] != 0:
			return board[x][0]

	for x in range(0,3):
		column = set([board[0][x],board[1][x],board[2][x]])
		if len(column) == 1 and board[0][x] != 0:
			return board[0][x]

	diagonal1 = set([board[0][0],board[1][1],board[2][2]])
	diagonal2 = set([board[0][2], board[1][1], board[2][0]])
	if len(diagonal1) == 1 or len(diagonal2) == 1 and board[1][1] != 0:
		return board[1][1]

	return 0