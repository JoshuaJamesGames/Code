#Develop a Python application that incorporates using appropriate data types 
# and provides program output in a logical manner.  Your program should 
# prompt a user to enter a car brand, model, year, starting odometer reading, 
# an ending odometer reading, and the estimated miles per gallon consumed by 
# the vehicle. Store your data in a dictionary and print out the contents of 
# the dictionary.

from enum import auto


automobile = {} #An empty Dictionary
#Collect information from the user by prompting and assigning responses to keys
#Using formatted strings to make the prompts more lively
automobile['car_brand'] = input("Please enter a car brand. : ")
automobile['car_model'] = input(f"Please enter the {automobile['car_brand']} model : ")
automobile['car_year'] = input(f"What year is the {automobile['car_model']}? : ")
automobile['odometer_start'] = input("What is the starting odometer reading? : ")
automobile['odometer_end'] = input("What is the ending odometer reading? : ")
automobile['estimated_mpg'] = input(f"Estimated number of miles per gallon for the {automobile['car_brand']} {automobile['car_model']}? : ")
#Now to print it all out
#Using 3 lines to keep the length managable and formatted strings so they are easier to read
print(f"You entered a {automobile['car_year']} {automobile['car_brand']} {automobile['car_model']}.")
print(f"The vehicle has a starting odometer reading of {automobile['odometer_start']} and an ending odometer reading of {automobile['odometer_end']}.")
print(f"You believe it gets {automobile['estimated_mpg']} MPG")