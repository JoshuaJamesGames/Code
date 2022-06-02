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
import java.util.ArrayList;

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
            System.out.print("\nWhat would you like to do?: ");
            selectedOption = scnr.next();
        

            if (selectedOption.equals("1")){

                addAuto(inventory, makeAuto());

            }else if (selectedOption.equals("2")){

                System.out.println("\nWhat vehicle would you like to remove?: ");
                remAuto(inventory, selectAuto(inventory));
                
            }else if (selectedOption.equals("3")){

                String selectedAuto = selectAuto(inventory);
                if(!selectedAuto.equals("null")){
                    updateAuto(inventory, selectedAuto, selectAttribute(inventory, selectedAuto));
                }
                
            }else if (selectedOption.equals("4")){

                showInventory(inventory);

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
        String year;
        String mileage;

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
        year = scnr.next();
        System.out.print("Finally, how many miles does it have?: ");
        mileage = scnr.next();
        System.out.printf("\nAdding a %s %s %s made in %s with %s miles.\n", 
                            color, make, model, year, mileage);
        
        return new Automobile(make, model, color, year, mileage);
    }

    public static String autoHash(Automobile auto){
        
        String hash = Integer.toString(auto.hashCode());
        return hash;
    }

    public static void addAuto(
        HashMap<String, Automobile> inventory, Automobile auto){
            
        inventory.put(autoHash(auto), auto);
    }

    public static void remAuto(
        HashMap<String, Automobile> inventory, String key){
        if(!key.equals("null")){
            System.out.printf("Removing %s\n",inventory.get(key));  
            inventory.remove(key);     
        }    
                   
    }

    public static String selectAuto(HashMap<String, Automobile> inventory){
        ArrayList<String> keyList = new ArrayList<String>();
        int selectedKey = -1;
        Scanner scnr = new Scanner(System.in);

        if(inventory.size()>0){        
            
            
            for(int i = 0; i < inventory.size(); i++){
                keyList.add(inventory.keySet().toArray()[i].toString());
                System.out.println("("+ (i+1) +") " + inventory.values().toArray()[i]);
            }   
            
            System.out.print("\nSelect a vehicle Number 1-" + keyList.size() + ": ");
            selectedKey = scnr.nextInt();
            return keyList.get(selectedKey - 1);
        }else{
            System.out.println("\nNo Inventory! You need to add a vehicle.");
            return "null";
        }
        
    }

    public static String selectAttribute(
        HashMap<String, Automobile> inventory, String key){
        Scanner scnr = new Scanner(System.in);
        int attributeSelected = -1;

        HashMap<String, Object> selectedAutoDetails = inventory.get(key).getInfo();
        String keyList[] = new String[selectedAutoDetails.size()];
        System.out.println("\nVehicle attributes: ");
            
        for(int i = 0; i < selectedAutoDetails.size(); i++){
            keyList[i] = selectedAutoDetails.keySet().toArray()[i].toString();
            System.out.println("("+ (i+1) +") " + keyList[i] +" : "+ selectedAutoDetails.values().toArray()[i]);
        }
        
        System.out.print("What attribute would you like to update?: ");
        attributeSelected = scnr.nextInt();

        return keyList[attributeSelected-1];
    }

    public static void updateAuto(
        HashMap<String, Automobile> inventory, String key, String attribute){

        Scanner scnr = new Scanner(System.in);
        HashMap<String, Object> selectedAutoDetails = inventory.get(key).getInfo();

        String oldValue = selectedAutoDetails.get(attribute).toString();
        //String valueKey = selectedAutoDetails.keySet().toArray()[attribute].toString();
        
        System.out.printf("You have selected %s with a value of %s.\n", attribute, oldValue);
        System.out.print("What is the new value?: ");
        
        String newValue = scnr.next();

        System.out.printf("Updating %s to %s.\n", attribute, newValue);

        inventory.get(key).updateInfo(attribute, newValue);      
        
    }

    public static void showInventory(HashMap<String, Automobile> inventory){
        
        if(inventory.size()>0){
            System.out.println("\nCurrent Vehicle Inventory is: ");
            
            for(int i = 0; i < inventory.size(); i++){
            
                System.out.println("("+ (i+1) +") " + inventory.values().toArray()[i]);
            }   
            
        }else{
            System.out.println("\nNo Inventory! You need to add a vehicle.");
        }

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
            String year,
            String mileage){

            this.make = make;
            this.model = model;
            this.color = color;
            this.year = Integer.valueOf(year);
            this.mileage = Integer.valueOf(mileage);          

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

        public void updateInfo(String key, String value){
            
                switch(key){
                    case "make":
                        this.make = value;
                    break;
                    case "model":
                        this.model = value;
                    break;
                    case "color":
                        this.color = value;
                    break;
                    case "year":
                        this.year = Integer.valueOf(value);
                    break;
                    case "mileage":
                        this.mileage = Integer.valueOf(value);
                    break;
                }
        }

        public String toString(){
            return (String.format("%d %s %s %s with %d miles.", 
                this.year, this.color, this.make, this.model, this.mileage));
            
        }

    }
}
