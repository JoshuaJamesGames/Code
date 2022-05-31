/*
Create an automobile class that will be used by a dealership as a vehicle 
inventory program. The following attributes should be present in your 
automobile class:

private string make
private string model
private string color
private int year
private int mileage.

Your program should have appropriate methods such as:
-Constructor
-Parameterized constructor
-Add a new vehicle  method
-List vehicle information (return string array)
-Remove a vehicle method
-Update vehicle attributes method.

All methods should include try..catch constructs. Except as noted all methods 
should return a success or failure message (failure message defined in "catch").

Create an additional class to call your automobile class (e.g., Main or 
AutomobileInventory). Include a try..catch construct and print it to the 
console.

Call automobile class with parameterized constructor (e.g., "make, model, 
color, year, mileage").
-List the values. Loop through the array and print to the
screen.

Call the remove vehicle method to clear the variables.
-Print the return value.

Add a new vehicle.
-Print the return value.
-Call the list method and print the new vehicle information to the screen.

Update the vehicle.
-Print the return value.
-Call the listing method and print the information to the screen.

Display a message asking if the user wants to print the information to a file 
(Y or N).
-Use a scanner to capture the response. If "Y", print the file to a predefined 
location (e.g., C:\Temp\Autos.txt). Note: you may want to create a method to 
print the information in the main class.
If "N", indicate that a file will not be printed.

*/
import java.util.Scanner;
import java.util.HashMap;

public class CSC320_Portfolio_Project_Option1 {
    public static void main(String[] args) {
        String selectedOption = "";
        HashMap<String, Automobile> inventory = new HashMap<String, Automobile>();
        Scanner scnr = new Scanner(System.in);

        System.out.println("Welcome to the Vehicle Inventory Program!");
        System.out.println("Select an option for the list.");
        while(!selectedOption.equals("q")){
            System.out.println("\n(1) Add new vehicle.");
            System.out.println("(2) Remove a vehicle.");
            System.out.println("(3) Update a vehicle.");
            System.out.println("(4) View inventory.");
            System.out.println("(q) Quit the program.");
            System.out.print("What would you like to do?: ");
            selectedOption = scnr.next();
        

            if (selectedOption.equals("1")){

            }else if (selectedOption.equals("2")){

            }else if (selectedOption.equals("3")){

            }else if (selectedOption.equals("4")){

            }else if (selectedOption.equals("q")){
                System.out.println("\nGoodbye!");
            }else{
                System.out.println("\nThat option isn\'t on the list.");
            }
        }
        scnr.close();
    
    }

    public static Automobile makeAuto(){
        Scanner scnr = new Scanner(System.in);
        String make;
        String model;
        String color;
        int year;
        int mileage;

        System.out.println("\nLet\'s make an automobile!");
        System.out.println("I\'ll walk you through the details.\n");
        System.out.print("Who made the car? (It\'s make): ");
        make = scnr.next();
        System.out.printf("What type of %s is it? (The model): ", make);
        model = scnr.next();
        System.out.printf("What color is the %s %s?: ", make, model);
        color = scnr.next();
        System.out.printf(
            "So far, you have entered a %s %s %s.\nWhat year was it made?: ", 
                            make, model, color);
        year = scnr.nextInt();
        System.out.print("Finally, how many miles does it have?: ");
        mileage = scnr.nextInt();
        System.out.printf("\nAdding a %s %s %s made in %d with %d miles.", 
                            color, make, model, year, mileage);
        scnr.close();
        return new Automobile(make, model, color, year, mileage);
    }

    public static String autoHash(Automobile auto){

    }

    public static class Automobile{

        private String make;
        private String model;
        private String color;
        private int year;
        private int mileage;

        public Automobile(
            String make,
            String model,
            String color,
            int year,
            int mileage){

            this.make = make;
            this.model = model;
            this.color = color;
            this.year = year;
            this.mileage = mileage;          

        }

        public HashMap<String, Object> getInfo(){
            
            HashMap<String, Object> autoInfo = new HashMap<String, Object>();
            autoInfo.put("make", this.make);
            autoInfo.put("model", this.model);
            autoInfo.put("color", this.color);
            autoInfo.put("year", this.year);
            autoInfo.put("mileage", this.mileage);

            return autoInfo;
        }

    }
}
