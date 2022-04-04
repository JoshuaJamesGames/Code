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
        self.__make = str(make)
        self.__model = str(model)
        self.__color = str(color)
        self.__year = int(year)
        self.__mileage = int(mileage)
    def get_info(self):
        return [self.__make, self.__model, self.__color, self.__year, self.__mileage]
    def update_info(self, make, model, color, year, mileage):
        self.__make = str(make)
        self.__model = str(model)
        self.__color = str(color)
        self.__year = int(year)
        self.__mileage = int(mileage)


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
    year = input('What year was it made?: ')
    mileage = input('Finally, how many miles does it have?: ')
    print(f'\nAdding a {color} {make} {model} made in {year} with {mileage} miles.')
    try:
        new_auto = Automobile(make, model, color, year, mileage)
    except ValueError:
        print('Something is wrong with those values! Try again.')
        new_auto = make_auto()

    return new_auto

def auto_hash(auto):
    hash_prefix = ''.join(str(attrib)[0] for attrib in auto.get_info())
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
        try:    
            vehicle_selected = selection_list[int(input('Please select a vehicle number: '))-1]
            
        except (ValueError, IndexError):
            print('That is not on the list.')
            vehicle_selected = select_auto(inventory)

        return vehicle_selected  
    else:
        print('\nNo Inventory! You need to add a new vehicle.')  
            
    

def rem_auto(inventory, auto_key):
    if auto_key:
        vehicle_stats = inventory[auto_key].get_info()
        print(f'Removing  {vehicle_stats[3]} {vehicle_stats[2]} {vehicle_stats[0]} {vehicle_stats[1]} with {vehicle_stats[4]} miles')
        del inventory[auto_key]

def select_attribute(inventory, auto_key):
    if auto_key:
        attribute_list = inventory[auto_key].get_info()
        print('\nVehicle attributes: ')
        for index, attribute in enumerate(attribute_list):
            print(f'({index+1}) {attribute}')
        try:    
            attribute_selected = int(input('\nSelect an attribute to update: ')) -1
            attribute_list[attribute_selected]

        except (ValueError, IndexError):
            print('That is not an attribute on the list.')
            attribute_selected = select_attribute(inventory, auto_key)

        return attribute_selected


def update_auto(inventory, auto_key, attribute_selected):
    if auto_key:
        vehicle_stats = inventory[auto_key].get_info()
        vehicle_keys = ['make', 'model', 'color', 'year', 'mileage']
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
            vehicle_stats = vehicle.get_info()
            print(f'({number+1}) {vehicle_stats[3]} {vehicle_stats[2]} {vehicle_stats[0]} {vehicle_stats[1]} with {vehicle_stats[4]} miles')
    else:
        print('\nNo Inventory! You need to add a new vehicle.')

def save_inventory(inventory):
    save_response = input('Would you like to save the inventory? (Y/N): ')
    if save_response.lower() == 'y':
        save_file = open('ITS320_Auto_Inventory.txt', 'w')
        if len(inventory) > 0:
            save_file.write('Current Saved Inventory includes:\n')
            for number, (key, vehicle) in enumerate(inventory.items()):
                vehicle_stats = vehicle.get_info()
                save_file.write(f'({number+1}) {vehicle_stats[3]} {vehicle_stats[2]} {vehicle_stats[0]} {vehicle_stats[1]} with {vehicle_stats[4]} miles\n')
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
            break
        else:
            print('That option isn\'t on the list')




if __name__ == '__main__':
    main()