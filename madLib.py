##1 Project: Mad libs Python project.
#My Idea:
#Make a "chat robot" that will take a few input, and play around with them.
#Indput: Name, Last name, Age, Profession
#Output: Hello Full name, A pressention of the age and profession. Scamble name.

import datetime
from time import sleep

#The chat 'Robot'

today = datetime.date.today()


print('Hello and welcome to the Mad libs Chat robot \n')
firstName = input('Let me start by kindly ask for your First Name: \n')
lastName = input('Welll Hallo: ' + firstName + ' please what is your last name? \n')
inputAge = input('Well hallo ' + firstName + ' ' + lastName + ' How old are you? ')
age = int(inputAge)
print (type(age))
print (type(today.year))
yearOfBirth = str(age-today.year)
profession = input('Wow, so you must have been born around' + yearOfBirth + ' \nSo let me know, what are you doing in your daily work? \n')
print('Okay thats sound cool. Well are you up for a little play?\n')
inputRandom = input('Please give me a random number between 1 and ' + str(len(firstName)) +' ' )
inputRandom = int(inputRandom)
newFirstName = firstName[0:inputRandom] + firstName[inputRandom].upper() + firstName[inputRandom +1:len(firstName)]
print(newFirstName+ ' ' + lastName)
inputRandomtwo = input('Hah, saw you that??? let mess up you last name too \n Please give me a random number between 1 and ' + str(len(lastName)) + ' ')
inputRandomtwo = int(inputRandomtwo)
newLastName = lastName[0:inputRandomtwo] + lastName[inputRandomtwo].upper() + lastName[inputRandomtwo +1:len(lastName)]
print(newFirstName + ' ' + newLastName)
print('Well maybe im not a BIG TECH AI, but i think I can do some funny things with you full name')
sleep (0.6)
print('Well let me first fix you name back to some more normal stuff :) ')
sleep (0.6)
print(' Bim')
sleep (0.6)
print('Bam')
sleep (0.6)
print('Busse')
sleep (0.6)
print (firstName.title() + ' ' + lastName.title() + ' Are you happy now???')
sleep(0.6)
print('Ok lets talk a little about your work \n')
sleep(0.6)
hours = int(input('So how many hours do you work each week??? '))
sleep(0.6)
print('did you know thats roughly ' + str(hours*4) +  ' hours per mounth!!!')
sleep(0.6)
print('if thats the case, please at least tell me you make good money for that amount of hours??? \n How much do you earn each mount?')
payment = int(input())
print('Well thats okay I guess, well at least compaired to what you are telling me :) but wanna know some fun fact about your working life??? \n')
sleep(0.6)
print('you get ' + str(payment/4) + ' DKK each week:)')
sleep(0.6)
print('or if you really want to know what you are worth each hour')
print(str((payment/4)/hours) + ' DKK')
print('SAY WHAT? THATS a crazy number, im pretti sure you bank will be confused to see that kind of number in their system. Please let me fix that')
sleep(0.6)
print('Ahh here you go: ' +str(payment*360) + ' DKK')
sleep(0.6)
print('Oig! Thats not right, please give me a sec')
sleep(0.6)
print('Ahh yes, here are a more normal number :) ')
print(round(((payment/4)/hours),2 ))



