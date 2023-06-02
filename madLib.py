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
print(' Bim \n Bam \n Busse')
sleep (0.6)
print (firstName.title + ' ' + lastName.title() + ' Are you happy now???')

