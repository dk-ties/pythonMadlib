import random


""" 2 Project: Guess the number (vs computer)
My Idea:
Create a small guess the number, just in terminal
Output some print,
Input a guess
Output if it correct, or needs to be warmer or colder. """

""" 
computerGuess = Random number between 0-10 
input player guess 
    Transform to integer
    Check if between 0-10
Create computerGuess
    Randoom number between 0-10 Store it.
    Check if is == to computerGuess
        Player wins
        
    If not  
            lowver ask for new number with message of hotter
    if not
            Higher ask for new number with message of colder
    Guess correct start new game
    
Play up to 5 before exit game.
"""

""" playerGuess = int(input("Please write a number between 0-10 "))
if playerGuess > 10 or playerGuess < 0:
    print("Ohh looks like your number is not between 0-10 ")
    playerGuess = input("Please wirte a number between 0-10 ")
computerGuess =  random.randint(0,10)
print(computerGuess)

if playerGuess > computerGuess:
    print("Ohh you are close are you, try a bit warmer")
elif playerGuess < computerGuess:
        print("Ohh close one, try a bit colder")
elif playerGuess == computerGuess:
        print("BOOOOM you nailed it GOOD JOB")
quit() """

def getPlayerGuess():
    getPlayerGuessStatus = True
    
    while getPlayerGuessStatus == True:
        playerGuess = input("Please write a number between 0-10 ")
        try: 
            print('Ohh it looks like you wrote a number')
            playerGuess = int(playerGuess)
            if playerGuess > 10 or playerGuess < 0:
                    continue
            else:
                getPlayerGuessStatus = False
            print(f'Here it is :) {playerGuess}')
        except:
            print("Ohh did you not enter a number?")
            print(playerGuess)
            continue
    return(playerGuess)
print(getPlayerGuess())



gameScore = True
computerGuess =  random.randint(0,10)
print(computerGuess)
gameScore = 0
while gameScore < 5:
        playerGuess = getPlayerGuess()
        if playerGuess < computerGuess:
            print("Ohh you are close are you, try a bit warmer")
            continue
        elif playerGuess > computerGuess:
            print("Ohh close one, try a bit colder")
            continue
        elif playerGuess == computerGuess:
            print("BOOOOM you nailed it GOOD JOB")
            gameScore = gameScore+1
            print(f'Score:  {gameScore}')
            computerGuess =  random.randint(0,10)
            print(computerGuess)
print('And you are the BIG WINNER!!!!!')
