#4 Rock, paper, scissors
#My Idea: Simply Rock, Paper and Scissors game vs computer.
#Game loop with best of 5.
import random


#Overall Varib
choises = ['rock', 'paper', 'scissor']

#PsudoCode

#function for pcPick
def compPickFunction():
    choice = random.randint(1,3) 
    if choice == 1:
        choice = 'rock'
    elif choice == 2:
        choice = 'paper'
    elif choice == 3:
        choice = 'scissor'
    return(choice)

print(compPickFunction())

#Function for plPick
def PlayerPickFunction():
    while True:
        playerChoice = input(f'Please choose:{choises}')
        playerChoice = playerChoice.lower()
        try:
            if playerChoice in choises:
             break
        except:
            print(f'Oh please pick one of the possible choicse {choises}')
            continue
    return (playerChoice)
            
print(PlayerPickFunction())




#Game loop
""" 
gameRound = 0
computerPoint = 0
playerPoint = 0

while gameRound < 5: 
    pcPick = compPickFunction()
    plPick = PlayerPickFunction()
        if pcPic == plPick
            continue
        elif pcPic = rock and plPick = paper
            playerPoint += 1
            print(f'HepHey Player win: {playerPoint}/5')
            break
        elif pcPic = paper and plPick = Scissor
            print(f'HepHey Player win: {playerPoint}/5')
            playerPoint += 1
            break
        elif pcPic = scissor and plPick = rock
            print(f'HepHey Player win: {playerPoint}/5')
            playerPoint += 1
            break
        else
            print(f'HepHey Player win: {computerPoint}/5')
            computerPoint += 1
            break
    gameRound += 1
        
"""