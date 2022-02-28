#Create a program that will calculate the weekly average tax witholding for a customer
#given the folling weekly income guidelines
#Income less than/equal to $500: tax rate 10%
#Income greater than/equal to $1500 and less than $2500: tax rate 20%
#Income greater than/equal to $2500: tax rate 30%

#Store the income brackets and rates in a dictionary
#Write a statement that prompts the user for an income, looks up the tax rate
#then prints up the income, tax rate, and tax

#Set up the income brackets and rates
#Using integer keys and values so I can parse them later
tax_brackets = {
    500:10,
    1500:20,
    2500:30
}

#Get input from the user with a prompt
print('This program will tell you what your tax rate and taxes are based on your input.')
user_income = input('What is your weekly income?: ')
