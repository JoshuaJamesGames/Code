#Develop a Python application that incorporates using appropriate data types 
# and provides program output in a logical manner.  Your program should 
# prompt a user to enter a car brand, model, year, starting odometer reading, 
# an ending odometer reading, and the estimated miles per gallon consumed by 
# the vehicle. Store your data in a dictionary and print out the contents of 
# the dictionary.

automobile = {} #An empty Dictionary
#Collect information from the user by prompting and assigning responses to keys
#Using formatted strings to make the prompts more lively
#Each field is dynamically typed by Python so I don't need to convert between str() and int()
#If I need to do math - I would have to be much more careful
automobile['car_brand'] = input("Please enter a car brand. : ")
automobile['car_model'] = input(f"Please enter the {automobile['car_brand']} model : ")
automobile['car_year'] = input(f"What year is the {automobile['car_model']}? : ")
automobile['odometer_start'] = input("What is the starting odometer reading? : ")
automobile['odometer_end'] = input("What is the ending odometer reading? : ")
automobile['estimated_mpg'] = input(f"Estimated number of miles per gallon for the {automobile['car_brand']} {automobile['car_model']}? : ")

#Now to print it all out
#Using 3 lines to keep the length managable and formatted strings so they are easier to read
#Started with a \n (NewLine) to space out the input and output

print(f"\nYou entered a {automobile['car_year']} {automobile['car_brand']} {automobile['car_model']}.")
print(f"The vehicle has a starting odometer reading of {automobile['odometer_start']} and an ending odometer reading of {automobile['odometer_end']}.")
print(f"You believe it gets {automobile['estimated_mpg']} MPG")

#I don't know if you read all the comments, but your announcement to not use the 'itertools'
#module prompted me to look it up out of curiosity.  The search triggered an invite for
#Google's FooBar Challenge - super awesome!