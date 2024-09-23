import random

def printBoard(board): # in bảng
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('You want to be X or O ?')
        letter = input().upper()
    if letter == 'X': return ['X', 'O']
    else: return ['O', "X"]

def whoGoFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else: return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(loc, chr): # xác định điều kiện thắng
    return((loc[7] == chr and loc[8] == chr and loc[9] == chr) or
    (loc[4] == chr and loc[5] == chr and loc[6] == chr) or
    (loc[1] == chr and loc[2] == chr and loc[3] == chr) or
    (loc[7] == chr and loc[4] == chr and loc[1] == chr) or
    (loc[2] == chr and loc[8] == chr and loc[5] == chr) or
    (loc[3] == chr and loc[6] == chr and loc[9] == chr) or
    (loc[1] == chr and loc[5] == chr and loc[9] == chr) or
    (loc[7] == chr and loc[5] == chr and loc[3] == chr))

def getBoardCopy(board):# tạo bản sao của mảng board
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move): #kiểm tra mảng có trống không
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else: return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X': playerLetter = 'O'
    else: playerLetter = 'X'

    for i in range(1, 10): #kiểm tra xem máy có thể thắng trong nước tiếp theo không ?
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10): #kiểm tra xem người có thể thắng trong nước tiếp theo không và block chết cmn :)
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9]) # chọn 1 trong 4 góc nếu trống
    if move != None: return move

    if isSpaceFree(board, 5): return 5 # chọn ô trung tâm nếu trống

    return chooseRandomMoveFromList(board, [2, 4, 6, 8]) # chọn bất kỳ ô nào còn trống

def isBoardFull(board):
    for i in range (1,10):
        if isSpaceFree(board, i): return False
    return True

print('Welcome to Tic-Tac_Toe!')
while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoFirst()
    print('The ' + turn + ' will go first.')
    isOK = True
    while isOK:
        if turn == 'player':
            printBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                printBoard(theBoard)
                print('YOU WON!')
                isOK = False
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print('TIE!')
                    break
                else: turn = 'computer'
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                printBoard(theBoard)
                print('YOU LOSE!')
                isOK = False
            else:
                if isBoardFull(theBoard):
                    printBoard(theBoard)
                    print('TIE!')
                    break
                else: turn = 'player'
    
    print('PLAY AGAIN? (yes or no)')
    if not input().lower().startswith('y'): break