import random

print('What\'s your name?: ')
myName = input()

guessesTaken = 0
number=random.randint(1, 20)

print('Well ' + myName + ', I am thinking of a number between 1 and 20.' )
guess = 0
for guessesTaken in range (6):
    print('Take a guess')
    guess=int(input())

    if guess > number:
        print('Your guess is too high.')
    elif guess < number:
        print('Your guess is too low.')
    else: break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')