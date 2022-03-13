#Write a Python function that will work on three strings. 
#The function will return to the user a concatenation of the string values in 
#reverse order. 
#The function is to be called from the main program.

#In the main program, prompt the user for the three strings and pass these 
#values to the function.

#First, a place for our string collection
strings_to_reverse = []

#Amount of times we will ask for strings
num_of_strings = 3

#Some output to get the user ready to input some strings
print(f'I will ask you for {num_of_strings} words.')
print('Once I have collected the words, I will reverse each word,')
print('reverse their order, concatenate them, and output the result.\n')

#A for loop to collect input from the user with prompts
#Start at 1 and end at num_of_strings
for index in range(1,num_of_strings+1):
    strings_to_reverse.append(input(f'Enter string #{index}: '))
print()


#The double_reverse function
def double_reverse(string_list):
    double_reversed_string = '' #Store our result here
    for string in reversed(string_list): #Going in reverse
        double_reversed_string +=string[::-1] #Using slice notation
    return double_reversed_string

#Output the results using double_reverse()
print(f'The double reversed concatenation of your strings is : {double_reverse(strings_to_reverse)}')
