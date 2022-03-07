#Write a program that will provide important statistics for the grades in a class.  
# The program will utilize a loop to read five floating-point grades from user input. 
#Ask the user to enter the values, then print the following data:
#   Average
#   Maximum
#   Minimum

#Somewhere to put all these grades
class_grades = []

#Inform the user of thier purpose
print('I will ask you for 5 grades and then output some statistics.')
print('Please use numbers, output will be in decimal format.')
#The input loop
for grade in range(1,6):
    class_grades.append(float(input(f'What is grade #{grade}: ')))

#This one prints the grade average
print(f'\nThe average of the grades is: {sum(class_grades)/5}')
#This prints the Maximum
print(f'The maximum grade is: {sorted(class_grades,reverse=True)[0]}')
#And the Minimum
print(f'The minimum grade is: {sorted(class_grades)[0]}')