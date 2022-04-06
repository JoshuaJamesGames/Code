#Create a final program that meets the requirements outlined below.

#Create an automobile class that will be used by a dealership as a vehicle inventory program.  
#The following attributes should be present in your automobile class:
#private string make
#private string model
#private string color
#private int year
#private int mileage
#Your program should have appropriate methods such as:

#constructor
#add a new vehicle
#remove a vehicle
#update vehicle attributes
#At the end of your program, it should allow the user to output all vehicle inventory to a text file.

#Import time & random for a simple hash function
from time import time
from random import random

#The class Automobile with an init method , getter, and setter
#Instead of individual methods for each attribute, I used a
#monolithic style to save space here and in the update_auto() method
class Automobile:

    #Initializes and casts types to the attributes
    def __init__(self, make, model, color, year, mileage):
        self.__make = str(make)
        self.__model = str(model)
        self.__color = str(color)
        self.__year = int(year)
        self.__mileage = int(mileage)
        
    #Returns an array of attributes
    def get_info(self):
        return {'make':self.__make, 'model':self.__model, 'color':self.__color, 'year':self.__year, 'mileage':self.__mileage}
        
    #update_info mirrors the __init__ method
    def update_info(self, make, model, color, year, mileage):
        self.__make = str(make)
        self.__model = str(model)
        self.__color = str(color)
        self.__year = int(year)
        self.__mileage = int(mileage)
    
    def __str__(self):
        return f"{self.__year} {self.__color} {self.__make} {self.__model} with {self.__mileage} miles"
        
#Walks the user through the creation of an Automobile object
def make_auto():
    #Create empty variables before filling them with input from user
    make = ''
    model = ''
    color = ''
    year = 0
    mileage = 0

    #Interactive creation processs!
    #The user is asked a series of questions to input each automobile
    print('\nLet\'s add an automobile!')
    print('I\'ll walk you through the details.\n')
    make = input('Who made the car? (It\'s make): ')
    model = input(f'What type of {make} is it? (The model): ')
    color = input(f'What color is the {make} {model}?: ')
    print(f'So far, you have entered a {color} {make} {model}.')
    year = input('What year was it made?: ')
    mileage = input('Finally, how many miles does it have?: ')
    print(f'\nAdding a {color} {make} {model} made in {year} with {mileage} miles.')
    #Try/Except block when we actually cast the variables and create the object
    #If there is an error, it calls make_auto() recursively after feedback
    try:
        new_auto = Automobile(make, model, color, year, mileage)
    except ValueError:
        print('Something is wrong with those values! Try again.')
        new_auto = make_auto()

    return new_auto

#This was a great dive into database collision.  Hash functions try to create
#unique ID's - The accepted standards come from a set of information
#Some form of timestamp
#A Random element
#Pieces of the information being stored
#Information from the system (Usually the MAC address)
#I didn't use all of them, but chose Pieces of information
#combined with a timestamp and random number
def auto_hash(auto):    
    #Need to convert the dictionary to a list for the next line
    auto_values = list(auto.get_info().values())
    #First letter of each of the attributes concatenated
    hash_prefix = ''.join(str(attrib)[0] for attrib in auto_values)
    #Time is in milliseconds since 1970 (Big Number) and a decimal
    #Random is a long decimal between 0 and 1 
    #Both are combined into a shorter ID with no decimal places
    hash_suffix = f'{(time()+random()*10000)%10000000:.0f}'
    return hash_prefix + hash_suffix

#This adds an Automobile with a generated Unique ID from auto_hash()
def add_auto(inventory, auto):
    inventory.update({auto_hash(auto):auto})    

#This displays the list of inventory and returns the selected ID
def select_auto(inventory):  
    #Variables to construct the list from unordered dictionary
    #and car is set to none originally  
    selection_list = []
    vehicle_selected = None
    
    #If there are automobiles in the list print them out with numbers
    if len(inventory) > 0:   
        print('\nThe current inventory is:')     
        for number, (key, vehicle) in enumerate(inventory.items()):        
            print(f"({number+1}) {vehicle}")
            selection_list.append(key)
        #vehicle_selected is set from the array built during the display of inventory
        #offset by 1 because it looks nice for the user instead of a 0-indexed list
        try:    
            vehicle_selected = selection_list[int(input('Please select a vehicle number: '))-1]
        #Standard errors found during my tests - Once again calls itself if there is an error   
        except (ValueError, IndexError):
            print('That is not on the list.')
            vehicle_selected = select_auto(inventory)

        return vehicle_selected
    #If there are no automobiles...  
    else:
        print('\nNo Inventory! You need to add a new vehicle.')              
    
#Once a key is selected. Remove the automobile from the inventory and give feedback
def rem_auto(inventory, auto_key):
    if auto_key:
        vehicle = inventory[auto_key]
        print(f'Removing {vehicle}')
        del inventory[auto_key]

#When updating an automobile, the user needs to pick which attribute to change
#This displays the list of current attribute values in a numbered list
def select_attribute(inventory, auto_key):
    if auto_key:
        #auto_stats is needed to display attributes and values
        auto_stats = inventory[auto_key].get_info()
        attribute_list = list(inventory[auto_key].get_info().values())
        print('\nVehicle attributes: ')
        for index, (attribute, value) in enumerate(auto_stats.items()):
            print(f'({index+1}) {attribute}: {value}')
        try:    
            attribute_selected = int(input('\nSelect an attribute to update: ')) -1
            attribute_list[attribute_selected]

        except (ValueError, IndexError):
            print('That is not an attribute on the list.')
            attribute_selected = select_attribute(inventory, auto_key)

        return attribute_selected


def update_auto(inventory, auto_key, attribute_selected):
    if auto_key:
        vehicle_stats = list(inventory[auto_key].get_info().values())
        vehicle_keys = list(inventory[auto_key].get_info().keys())
        old_value = vehicle_stats[attribute_selected]
        print(f'You have selected to update the {vehicle_keys[attribute_selected]}.')
        vehicle_stats[attribute_selected] = input(f'Current value is {vehicle_stats[attribute_selected]}, What is the new value?: ')
        print(f'Updating {vehicle_keys[attribute_selected]} from {old_value} to {vehicle_stats[attribute_selected]}')
        try:
            inventory[auto_key].update_info(*vehicle_stats)
        except ValueError:
            print('Something is wrong with that value!.')
            update_auto(inventory, auto_key, attribute_selected)
    

def show_inventory(inventory):    
    if len(inventory) > 0:
        print('\nCurrent Vehicle Inventory is: ')
        for number, (key, vehicle) in enumerate(inventory.items()):            
            print(f'({number+1}) {vehicle}')
    else:
        print('\nNo Inventory! You need to add a new vehicle.')

def save_inventory(inventory):
    save_response = input('Would you like to save the inventory? (Y/N): ')
    if save_response.lower() == 'y':
        save_file = open('ITS320_Auto_Inventory.txt', 'w')
        if len(inventory) > 0:
            save_file.write('Current Saved Inventory includes:\n')
            for number, (key, vehicle) in enumerate(inventory.items()):                
                save_file.write(f'({number+1}) ID# {key}: {vehicle}\n')
            save_file.close()
        else:
            print('\nNo Inventory!')
        

def main():
    selected_option = ''
    inventory = {}
    print('Welcome to the Vehicle Inventory Program!')
    print('Select an option from the list.')
    while selected_option != 'q':
        print('\n(1) Add new vehicle.')
        print('(2) Remove a vehicle.')
        print('(3) Update a vehicle.')
        print('(4) View inventory.')
        print('(q) Quit the program.')
        selected_option = input('What would you like to do?: ')

        if selected_option == '1':
            add_auto(inventory, make_auto())            
        elif selected_option == '2':
            rem_auto(inventory, select_auto(inventory))
        elif selected_option == '3':
            key = select_auto(inventory)
            attribute_num = select_attribute(inventory, key)
            update_auto(inventory, key, attribute_num)
        elif selected_option == '4':
            show_inventory(inventory)
        elif selected_option == 'q':
            save_inventory(inventory)
            print('Goodbye!')
            
        else:
            print('That option isn\'t on the list')




if __name__ == '__main__':
    main()