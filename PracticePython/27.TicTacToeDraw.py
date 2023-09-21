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