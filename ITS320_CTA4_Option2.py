#Write a program that will provide important statistics for the grades in a class.  
#The program will utilize a loop to read five floating-point grades from user input. 
#Ask the user to enter the values, then print the following data:
#   Average
#   Maximum
#   Minimum




#Somewhere to put all these grades
class_grades = []

#Inform the user of thier purpose and how the output will be floats
#We still aren't using input sanitation so I'm expecting accurate input
print('I will ask you for 5 grades and then output some statistics.')
print('Please use numbers, output will be in decimal format.')

#The input loop : 5 loops starting at 1 - Using the range index in the prompt
for grade in range(1,6):
    class_grades.append(float(input(f'What is grade #{grade}: ')))

#This one prints the grade average
print(f'\nThe average of the grades is: {sum(class_grades)/5}')

#This prints the Maximum
print(f'The maximum grade is: {sorted(class_grades,reverse=True)[0]}')

#And the Minimum
print(f'The minimum grade is: {sorted(class_grades)[0]}')

#Just an update from CTA2 because it's so awesome, and I am telling everyone.
#I have made it to level 3 of the Foobar challenges.
#Level 3 has 3 questions - I am on question 2.