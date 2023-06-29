#4 Rock, paper, scissors
#My Idea: Simply Rock, Paper and Scissors game vs computer.
#Game loop with best of 5.
import random


#Overall Varib
choises = ['rock', 'paper', 'scissor']

#PsudoCode

#function for pcPickkk
def compPickFunction():
    choice = random.randint(1,3) 
    if choice == 1:
        choice = 'rock'
    elif choice == 2:
        choice = 'paper'
    elif choice == 3:
        choice = 'scissor'
    return(choice)



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
            




#Game varibale

gameRound = 0
computerPoint = 0
playerPoint = 0

#Game Loop
while gameRound < 5: 
    print(f'We are at gameRound: {gameRound}')
    pcPick = compPickFunction()
    print(f'Pc have chosen {pcPick}')
    plPick = PlayerPickFunction()
    print(f'Player have chosen: {plPick}')
    #if pcPick Rock
    if pcPick == 'rock':
        print('pcPick is a Rock')
        if plPick == 'rock':
            print('Now i start a new round')
            continue
        elif plPick == 'paper':
            playerPoint += 1
            gameRound += 1
            continue
        elif plPick == 'scissor':
            computerPoint += 1
            gameRound += 1
            continue
    #if pcPick Paper
    elif pcPick == 'paper':
        print('pcPick is a Paper')
        if plPick == 'paper':
            print('Now i start a new round')
            continue
        elif plPick == 'scissor':
            playerPoint += 1
            gameRound += 1
            continue
        elif plPick == 'rock':
            computerPoint += 1
            gameRound += 1
            continue
    #if pcPick scissor
    elif pcPick == 'scissor':
        print('pcPick is a scissor')
        if plPick == 'scissor':
            print('Now i start a new round')
            continue
        elif plPick == 'rock':
            playerPoint += 1
            gameRound += 1
            continue
        elif plPick == 'paper':
            computerPoint += 1
            gameRound += 1
            continue


print(f'hepHey the result are: Player had: {playerPoint} while pc had: {computerPoint}')
quit()
    
    
    
    
    
    
    
""" 
    #Old Game loop
    if pcPick == plPick:
            print('NAHHH You chose the same, try again!')
            continue
    elif pcPick == 'rock' and plPick == 'paper':
            playerPoint += 1
            print(f'HepHey paper wins over Rock one point to: Player: {playerPoint}/5')
            break
    elif pcPick == 'paper' and plPick == 'scissor':
            print(f'HepHey scissor wins over Paper one point to: Player: {playerPoint}/5')
            playerPoint += 1
            break
    elif pcPick == 'scissor' and plPick == 'rock':
            print(f'HepHey Rock wins over Scissor one point to: Player: {playerPoint}/5')
            playerPoint += 1
            break
    else:
            print(f'HepHey Player win: {computerPoint}/5')
            computerPoint += 1
            break
    gameRound += 1
        
 """