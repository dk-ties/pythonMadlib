#Imports
import random
from words import words

#Variable
numberOfGuess = 0

#funtion to get a raondom word, from words.py
def randomWord():
    word = None
    randomNumber = random.randint(0, len(words))
    print(randomNumber)
    word = list(words[randomNumber])
    return word



print(f'Hello and wellcome to a game of Hangman. The computer have chosen a word for you to Guess. the word consist of {len(wordToGuess)} charector...')

#Function to get a guess.
def getGuess(numberOfGuess):
    
    while True:
        guess = input(f'Please type in your {numberOfGuess} guess ')
        if len(guess) > 1:
            print('Please only type one charector')
            continue
        else:
            break
    
    numberOfGuess += 1
    return guess
print(numberOfGuess)
print(getGuess(numberOfGuess))
print(numberOfGuess)
