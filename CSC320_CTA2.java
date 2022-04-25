/*
CSC320_CTA2 Option 1
Develop a Java application that provides program output in a logical manner 
and incorporates appropriate data types. Your program should prompt a user 
to enter a car brand, model, year, starting odometer reading, ending odometer 
reading, and gallons used. The output should include this information along 
with the estimated miles per gallon consumed by the vehicle in the format 
MPG: your calculation. 
Print each on separate lines with the appropriate labels (example, MPG: 25)
*/

import java.util.Scanner;

public class CSC320_CTA2 {
    public static void main(String[] args) {
        //Prompt user to enter vehicle information
        System.out.println("Let's make a vehicle!\n");
        Vehicle userVehicle = new Vehicle();
        //Output vehicle specs.
        System.out.println("\nThe vehicle information you input is: ");
        userVehicle.printSpecs();
        //Goodbye!
        System.out.println("\nGoodbye!");

    }

    public static class Vehicle{
        //Need to take input
        Scanner scnr = new Scanner(System.in);

        //Vehicle class attributes
        private String carBrand = "";
        private String carModel = "";
        private int carYear = 0;
        private int odometerStart = 0;
        private int odometerEnd = 0;
        private int gallonsUsed = 0;
        private double milesPerGallon = 0.0;

        //Constructor walks the user through vehicle creation interactively
        public Vehicle(){
            
            System.out.println("What is the make of the vehicle?: ");
            carBrand = scnr.next();
            System.out.println("What is the model of the " + carBrand + "?: ");
            carModel = scnr.next();
            System.out.println("What year was the " + carBrand + " " + carModel + " made?: ");
            carYear = scnr.nextInt();
            System.out.println("\nWe are going to calculate the MPG of the " + carYear + " " + carBrand + " " + carModel + ".");
            System.out.println("Please use whole numbers for the following questions.");
            System.out.println("What was the trip starting odometer reading?: ");
            odometerStart = scnr.nextInt();
            System.out.println("What was the trip ending odometer reading?: ");
            odometerEnd = scnr.nextInt();
            System.out.println("How many gallons of gas did the " + carModel + " use during the trip?: ");
            gallonsUsed = scnr.nextInt();
            
            //Calculate and store MPG
            milesPerGallon = (odometerEnd - odometerStart) / gallonsUsed;
        }

        public void printSpecs(){
            //Empty String for output
            String output;
            //Using format to make things nice and human-readable
            output = String.format(
                "Make: %s \n" +
                "Model: %s \n" +
                "Year: %s \n" +
                "Odometer Start: %d \n" +
                "Odometer End: %d \n" +
                "Gallons Used: %d \n" +
                "MPG: %.2f"            
            , carBrand, carModel, carYear, odometerStart, odometerEnd, gallonsUsed, milesPerGallon);
            System.out.println(output);
        } 
    }
}
