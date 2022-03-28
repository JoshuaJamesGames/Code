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


class Automobile:
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage

def add_auto():
    make = ''
    model = ''
    color = ''
    year = 0
    mileage = 0

    print('Let\'s add an automobile!')
    print('I\'ll walk you through the details.')
    make = input('Who made the car? (It\'s make): ')
    model = input(f'What type of {make} is it? (The model): ')
    color = input(f'What color is the {make} {model}?: ')
    print(f'So far, you have entered a {color} {make} {model}.')
    year = int(input('What year was it made?: '))
    mileage = int(input('Finally, how many miles does it have?: '))
    print(f'Adding a {color} {make} {model} made in {year} with {mileage} miles.')
    new_auto = Automobile(make, model, color, year, mileage)

    return new_auto

def __auto_hash(auto):
    pass

def rem_auto():

def update_auto():

def show_inventory():
    

def main():
    selected_option = ''
    inventory = {}
    print('Welcome to the Vehicle Inventory Program!')
    print('Select an option from the list.')
    while selected_option != 'q':
        print('(1) Add new vehicle.')
        print('(2) Remove a vehicle.')
        print('(3) Update a vehicle.')
        print('(4) View inventory.')
        print('(q) Quit the program.')
        selected_option = input('What would you like to do?: ')

        if selected_option == '1':
            add_auto()
        elif selected_option == '2':
            rem_auto()
        elif selected_option == '3':
            update_auto()
        elif selected_option == '4':
            show_inventory()
        else:
            print('That option isn\'t on the list')




if __name__ == '__main__':
    main()