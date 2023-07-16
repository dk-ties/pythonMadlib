#Imports
import random
from words import words

#Variable
numberOfGuess = 0

#funtion to get a raondom word, from words.py
def randomWord():
    word = None
    randomNumber = random.randint(0, len(words))
    #print(randomNumber)
    word = list(words[randomNumber])
    return word




#Function to get a guess.
def getGuess(numberOfGuess):
    
    while True:
        guess = input(f'Please type in your {numberOfGuess} guess ')
        if len(guess) > 1:
            print('Please only type one charector')
            continue
        else:
            break
    

    return guess

#Function to compare word to gues, with guess

def compareGuess(guess):
    wordPosi = None
    try: 
        wordPosi = wordToGuessBack.index(guess)
        #print(f'The char is on position {wordPosi}')
    except ValueError:
        print('That char is not a part of the word, please try again.')


    return wordPosi
#Game loop starting...

while True:
    wordToGuessBack = randomWord()
    wordtoGuessFront = ['x'*len(wordToGuessBack)]
    wordtoGuessFront = list(wordtoGuessFront[0])
    print(f'Backend word {wordToGuessBack}')
    print(f'Hello and wellcome to a game of Hangman. The computer have chosen a word for you to Guess. the word consist of {wordtoGuessFront} charector...')
    while numberOfGuess < 10:
        #print(type(wordtoGuessFront))
        #print(f'word to guess: {wordtoGuessFront}')        
        #print('Please enter a gues ')
        currentGuess = getGuess(numberOfGuess)
        currentGuessIndex = compareGuess(currentGuess)
        #print(f'the char you type have index number: {currentGuessIndex}')
        numberOfGuess += 1
        if currentGuessIndex == None:
            print('Oh seems that the chars is not part of the word, please try again ')
            continue
        else:
            print('So is im here or whats happening?')
            print(f'so on place you guess are currently this char {wordtoGuessFront[currentGuessIndex]}', currentGuess)
            wordtoGuessFront[currentGuessIndex] = currentGuess
            print(wordtoGuessFront)
            continue
    break
            
print(f'We got to the end of the game, and you need {numberOfGuess} to guess the word.') 


#print(numberOfGuess)
#print(getGuess(numberOfGuess))
#print(numberOfGuess)
