#Create a program that will calculate the weekly average tax witholding for a customer
#given the folling weekly income guidelines
#Income less than $500: tax rate 10%
#Income greater than/equal to $500 and less than $1500: tax rate 15%
#Income greater than/equal to $1500 and less than $2500: tax rate 20%
#Income greater than/equal to $2500: tax rate 30%

#Store the income brackets and rates in a dictionary
#Write a statement that prompts the user for an income, looks up the tax rate
#then prints up the income, tax rate, and tax

#Set up the income brackets and rates
#Using integer keys and values so I can parse them later
tax_brackets = {
'Less than 500': 10,
'500 to 1499': 15,
'1500 to 2499': 20,
'2500 or more': 30
}

#Initialize some variables
tax_rate = 0
tax = 0
tax_range = ""

#Get input from the user with a prompt
print('This program will tell you what your tax rate and taxes are based on your input.')

#We still haven't discussed input sanitation so I will assume perfect answers
#Convert string type to integer
user_income = int(input('What is your weekly income?: '))

#The classic if, elif..., else sequence
if user_income < 500:
    tax_rate = tax_brackets['Less than 500']
    tax_range = 'Less than $500'
elif (user_income >= 500) and (user_income <= 1499):
    tax_rate = tax_brackets['500 to 1499']
    tax_range = 'between $500 and $1499'
elif (user_income >= 1500) and (user_income <= 2499):
    tax_rate = tax_brackets['1500 to 2499']
    tax_range = 'between $1500 and $2499'
else:
    tax_rate = tax_brackets['2500 or more']
    tax_range = '$2500 or more'

#Calculate weekly taxes
tax = int((user_income/100)*tax_rate) 

#Output useful information!
print(f'\nYou make ${user_income} per week.')
print(f'That is ${user_income * 52} a year, before taxes.')
print(f'Your taxe rate is {tax_rate}%.')
print(f'That means you will pay ${tax} per week or ${tax*52} in taxes a year.')
print(f'After taxes, you will make ${(user_income - tax)} per week or ${(user_income - tax)*52} per year.')