import random


""" 3 Project: Guess the number (vs player)
My Idea:
Grab a copy of  small guess the number game, just in terminal
Output some print,
Input a guess
Output if it correct, or needs to be warmer or colder. 
switch round, after each succesfull guess"""

playerOne = {
    "round": 0 ,
    "guess": 0
}
playerTwo = {
    "round": 0 ,
    "guess": 0
}

print(playerOne["guess"])
print(playerTwo["guess"])



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


""" if playerOne.round < 5 and playerTwo.round < 5:
    gameScore = True
 """#computerGuess =  random.randint(0,10)

playerOne["guess"] = getPlayerGuess()
playerTwo["guess"] = getPlayerGuess()

while gameScore < 5:
    if playerOne["guess"] < playerTwo["guess"]:
        print("Ohh you are close are you, try a bit warmer")
        continue
    elif playerOne["guess"] > playerTwo["guess"]:
        print("Ohh close one, try a bit colder")
        continue
    elif playerOne["guess"] == playerTwo["guess"]:
        print("BOOOOM you nailed it GOOD JOB")
        gameScore = gameScore+1
        print(f'Score:  {gameScore}')
        computerGuess =  random.randint(0,10)
        print(computerGuess)
print('And you are the BIG WINNER!!!!!')




""" 
gameScore = 0
while gameScore True:
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
 """

""" How to make this to a two player game? """