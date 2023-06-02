##1 Project: Mad libs Python project.
#My Idea:
#Make a "chat robot" that will take a few input, and play around with them.
#Indput: Name, Last name, Age, Profession
#Output: Hello Full name, A pressention of the age and profession. Scamble name.

import datetime

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
#profession = input 
print('Wow, so you must have been born around' + yearOfBirth + ' \n')