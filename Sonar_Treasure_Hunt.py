import random
import sys
import math

def getNewBoard():
    # create a 60*15 board
    board = []
    for i in range(60):
        board.append([])
        for j in range(15):
            if random.randint(0, 1) == 0:
                board[i].append('~')
            else: board[i].append('`')
    return board

def drawBoard(board):
    # Draw the board data structure.
    tensDigitsLine = ' ' # Initial space for the numbers down the left side of the board
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    # Print the numbers across the top of the board.
    print(tensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()

    # Print each of the 15 rows.
    for row in range(15):

    # Single-digit numbers need to be padded with an extra space.
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''

        # Create the string for this row on the board.
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]
        print('%s%s %s %s' % (extraSpace, row, boardRow, row))
    # Print the numbers across the bottom of the board.
    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)


def getRandomChest(numChest):
    # Create a list contain chest's coordinates
    chests = []
    while len(chests) < numChest:
        newChest = [random.randint(0, 59), random.randint(0, 14)]
        if newChest not in chests: chests.append(newChest)
    return chests

def isOnBoard(x, y):
    # Check wheter the given coordinate is on the board or not
    return x >= 0 and x <= 59 and y >= 0 and y <= 14
 
def makeMove(board, chests, x, y):
    # Put the sonar device character on the board, remove treasure chests list as they are found.
    # Return false if this is an invalid move.
    # Otherwise, return the string of the result of this move.
    smallestDistance = 100 
    for cx, cy in chests:
        distance = math.sqrt((cx - x) ** 2 + (cy - y) ** 2)

        if distance < smallestDistance: # Update the distance of the closest chest.
            smallestDistance = distance
    smallestDistance = round(smallestDistance)

    if smallestDistance == 0: # (x, y) is the corrdinate of the chest.
        chests.remove([x, y])
        return 'You have found a sunken treasure chest!'

    elif smallestDistance < 10:
        board[x][y] = str(smallestDistance)
        return 'Treasure detected at a distance of {} from the sonar device.'.format(smallestDistance)

    else:
        board[x][y] = 'X'
        return 'Sonar did not detect anything. All treasure chests out of range.'

def getPlayerMove(previousMove):
    # Let the player enter their move,
    print('Where do u want to drop the next sonar device? (0 - 59, 0 - 14) (or type quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('Thanks for playing!')
            sys.exit()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMove:
                print('You already moved there.')
                continue
            return [int(move[0]), int(move[1])]
        print('Please enter a valid corrdinate')

def showInstructions():
    print('''Instructions:
    You are the captain of the Simon, a treasure-hunting ship. Your current mission is to use sonar devices to find three sunken treasure chests at the bottom of the ocean. But you only have cheap sonar that finds distance, not direction.

    Enter the coordinates to drop a sonar device. The ocean map will be marked with how far away the nearest chest is, or an X if it is beyond the sona device's range. For example, the C marks are where chests are. The sonar device shows a 3 because the closest chest is 3 spaces away.

               1         2         3
     012345678901234567890123456789012

    0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0  
    1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
    2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
    3 ````````~~~`````~~~`~`````~`~``~` 3
    4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

    012345678901234567890123456789012
              1         2         3
    (In the real game, the chests are not visible in the ocean.)

    Press enter to continue...''')
    input()

    print('''When you drop a sonar device directly on a chest, youretrieve it and the other sonar devices update to show how far away the next nearest chest is. The chests are beyond the range of the sonar device on the left, so it shows an X.

                 1         2         3
       012345678901234567890123456789012

     0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
     1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
     2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
     3 ````````~~~`````~~~`~`````~`~``~` 3
     4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

       012345678901234567890123456789012
                 1         2         3

    The treasure chests don't move around. Sonar devices can detect treasur chests up to a distance of 9 spaces. Try to collect all 3 chests before running out of sonar devices. Good luck!
    Press enter to continue...''')
    input()

print('S O N A R !')
print()
print('Would u like to view the instruction? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    # Setup
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChest(3)
    drawBoard(theBoard)
    previousMoves = []

    while sonarDevices > 0:
        # Show how many sonar device and unfound chests are.
        print('U have {} sonar device(s) left, {} treasure chest(s) remaining'.format(sonarDevices, len(theChests)))

        x, y = getPlayerMove(previousMoves)
        previousMoves.append([x, y])

        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False: 
            continue

        else:
            if moveResult == 'You have found a sunken treasure chest!':
                # Update all the sonar devices currently on the map.
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)
        if len(theChests) == 0:
            print('You have found all the sunken treasure chests! Congratulations and good game!')
            break
        sonarDevices -= 1
    
    if sonarDevices == 0:
        print('We\'ve run out of sonar devices! Now we have to turn the ship around and head')
        print('for home with treasure chests still out there! Game over.')
        print('     The remaining chests were here:')
        for x, y in theChests:
            print('{}, {}'.format(x, y))
        
    print('Do u want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        sys.exit()