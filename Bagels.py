import random

NUM_DIGITs = 3
MAX_GUESS = 10

def getSecretNum():
    #return a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITs):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secreatNum):

    if guess == secreatNum:
        return 'U got it!'

    rightNum, rightPlace = 0, 0
    for i in range(len(guess)):
        if guess[i] == secreatNum[i]:
            rightPlace += 1
        if guess[i] in secreatNum:
            rightNum += 1
    if rightNum == 0:
        return 'No digit right :(.'
    else:
        return 'You got {} digit right but only {} of them are in the right place.'.format(rightNum, rightPlace)
    

def isOnlyDigit(num):

    if num == '':
        return False

    for i in num:
        if i not in '0123456789':
            return False

    return True


print('I am thinking of a {}-digit number. Try to guess what it is.'.format(NUM_DIGITs))
#print('When I say:    That means:')
#print('  Bagels       None of the digits is correct.')
#print('  Pico         One digit is correct but in the wrong position.')
#print('  Fermi        One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('You have {}s guesses to get it.'.format(MAX_GUESS))

    guessesTaken = 1
    while guessesTaken <= MAX_GUESS:
        guess = ''
        while len(guess) != NUM_DIGITs or not isOnlyDigit(guess):
            print('Guess #{}: '.format(guessesTaken))
            guess = input()
        
        print(getClues(guess, secretNum))
        guessesTaken += 1

        if guess == secretNum: break

        if guessesTaken > MAX_GUESS: print('You ran out of guesses. The answer was {}'.format(secretNum))
    

    print('Do u want to play again? (yes or no)')
    if not input().lower().startswith('y'): break