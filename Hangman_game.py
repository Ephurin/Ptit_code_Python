import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
    o |
      |
      |
     ===''','''
  +---+
    o |
    | |
      |
     ===''','''
  +---+
    o |
   /| |
      |
     ===''','''
  +---+
    o |
   /|\|
      |
     ===''','''
  +---+
    o |
   /|\|
   /  |
     ===''', '''
  +---+
    o |
   /|\|
   / \| 
     ===''','''
  +---+
   [o |
   /|\|
   / \|
     ===''','''
  +---+
   [o]|
   /|\|
   / \|
     ===''']# vẽ hình 
words = {'Animals' : 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split()}
# tệp từ cho sẵn 
def getRandomWord(wordDict): # hàm lấy từ ngẫu nhiên
    wordKey = random.choice(list(wordDict.keys()))

    wordIndex = random.randint(0, len(wordDict[wordKey])-1)
    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):# hàm in kết quả ra màn hình
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:',end = ' ')
    for letter in missedLetters:# in các chữ cái đã đoán sai
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range (len(secretWord)):# thay thế khoảng '_' bằng các chữ cái đã đoán được
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    for letter in blanks:# in ra từ với các ký tự cách nhau 1 khoảng trống
        print(letter,end=' ')
    print()

def getGuess(alreadyGuesses):# trả về ký tự đã nhập, đảm bảo dữ liệu chỉ có 1 ký tự duy nhất
    while True:
        print('Guess a letter.')
        guess=input()
        guess=guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuesses:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please choose a LETTER.')
        else: return guess

def playAgain():# Trả về True nếu người chơi muốn chơi lại, còn lại trả về False
    print('Do u want to play again? (yes or no)')
    return input().lower() == 'yes'
# vào chương trình chính:
print('H A N G M A N')

difficulty = 'KKKK'
while difficulty not in 'EMH':
    print('Enter difficulty: E(easy), H(hard), M(medium)')
    difficulty = input().upper()                                   
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]                                           #chọn độ khó
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set {}'.format(secretSet))
    displayBoard(missedLetters, correctLetters, secretWord)
    
    guess = getGuess(missedLetters + correctLetters)# Nhập chữ cái mà người chơi dự đoán
    
    if guess in secretWord:
        correctLetters += guess
        # Kiểm tra người chơi đã thắng chưa
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters += guess
        # Kiểm tra xem người chơi đã đoán quá số lần quy định chưa
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else: break