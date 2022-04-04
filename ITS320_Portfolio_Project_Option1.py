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


class Automobile:
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage
    def get_info(self):
        return [self.__make, self.__model, self.__color, str(self.__year), str(self.__mileage)]

def make_auto():
    make = ''
    model = ''
    color = ''
    year = 0
    mileage = 0

    print('\nLet\'s add an automobile!')
    print('I\'ll walk you through the details.\n')
    make = input('Who made the car? (It\'s make): ')
    model = input(f'What type of {make} is it? (The model): ')
    color = input(f'What color is the {make} {model}?: ')
    print(f'So far, you have entered a {color} {make} {model}.')
    year = int(input('What year was it made?: '))
    mileage = int(input('Finally, how many miles does it have?: '))
    print(f'\nAdding a {color} {make} {model} made in {year} with {mileage} miles.')
    new_auto = Automobile(make, model, color, year, mileage)

    return new_auto

def auto_hash(auto):
    hash_prefix = ''.join(attrib[0] for attrib in auto.get_info())
    hash_suffix = f'{(time()+random()*10000)%10000000:.0f}'
    return hash_prefix + hash_suffix

def add_auto(inventory, auto):
    inventory.update({auto_hash(auto):auto})    

def select_auto(inventory):
    
    selection_list = []
    vehicle_selected = None
    
    if len(inventory) > 0:   
        print('\nThe current inventory is:')     
        for number, (key, vehicle) in enumerate(inventory.items()):
            vehicle_stats = vehicle.get_info()
            print(f'({number+1}) {vehicle_stats[3]} {vehicle_stats[2]} {vehicle_stats[0]} {vehicle_stats[1]} with {vehicle_stats[4]} miles')
            selection_list.append(key)
        vehicle_selected = int(input('Please select a vehicle number: ')) 
        return selection_list[vehicle_selected-1]   
    else:
        print('\nNo Inventory! You need to add a new vehicle.')  
            
    

def rem_auto(inventory, auto_key):
    if auto_key:
        vehicle_stats = inventory[auto_key].get_info()
        print(f'Removing  {vehicle_stats[3]} {vehicle_stats[2]} {vehicle_stats[0]} {vehicle_stats[1]} with {vehicle_stats[4]} miles')
        del inventory[auto_key]

def select_attribute(inventory, auto_key):
    attribute_list = inventory[auto_key].get_info()
    print('\nVehicle attributes: ')
    for index, attribute in enumerate(attribute_list):
        print(f'({index+1}) {attribute}')
    attribute_selected = int(input('\nSelect an attribute to update: '))
    return (attribute_selected -1)


def update_auto(inventory, auto_key, attribute_selected):

    pass

def show_inventory(inventory):    
    if len(inventory) > 0:
        print('\nCurrent Vehicle Inventory is: ')
        for number, (key, vehicle) in enumerate(inventory.items()):
            vehicle_stats = vehicle.get_info()
            print(f'({number+1}) {vehicle_stats[3]} {vehicle_stats[2]} {vehicle_stats[0]} {vehicle_stats[1]} with {vehicle_stats[4]} miles')
    else:
        print('\nNo Inventory! You need to add a new vehicle.')        

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
            print('Goodbye!')
            break
        else:
            print('That option isn\'t on the list')




if __name__ == '__main__':
    main()