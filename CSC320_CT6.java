/*
Option #2 - Create a Method to Return a String Array

Write program with a method that returns an array. The method should accept 
as input a comma-delimited string with three values from a user. 

The array should store each value in a different element. 

Use Try..Catch error handling and print any failure messages, or print 
success from within method if execution is successful 
(see Chapter 6 in the text). 

Call the method from the main method of the program to demonstrate its 
functionality by looping through the array and printing the individual values.
*/
import java.util.Scanner;

public class CSC320_CT6 {
    public static void main(String args[]){
        //Initialize
        final int numInputs = 3;
        String inputString = "";
        String userInput[] = new String[numInputs];
        Scanner scnr = new Scanner(System.in);

        //Intro
        System.out.println(String.format("Please Input %d Strings(Words), and I will repeat them.", numInputs));
        
        //Get Input from user
        inputString = buildInputString(numInputs, scnr);
        scnr.close();
        
        //Call method to store user's input into individual array elements
        System.out.println("\nStoring input...");

        userInput = inputToArray(inputString);
        
        //Print out array
        printArray(userInput, "String");

        //Outro
        System.out.println("\nGoodbye!");

    }

    public static String getInput(int inputNumber, String inputDescriptor, Scanner scnr){
        
        
        System.out.print(String.format("Please enter %s #%d: ", inputDescriptor, inputNumber));
        String response = scnr.next();
        
        return response;
    }

    public static String buildInputString(int numOfInputs, Scanner scnr){
        String userInputString = "";
        
        for(int i = 1; i <= numOfInputs; i++){
            userInputString += getInput(i, "String", scnr);
            if(i != numOfInputs){
                userInputString += ",";
            }
        }

        return userInputString;  
    }

    public static String[] inputToArray(String inputString){
        String output[] = new String[inputString.split(",").length];
        
        for(int i = 0; i < output.length; i++){
            output[i] = inputString.split(",")[i];
        }
        
        return output;
    }

    public static void printArray(String[] printme, String descriptor){
        System.out.println();
        for(int i = 0; i < printme.length; i++){            
            System.out.println(String.format("%s at index %d is %s.",descriptor, i, printme[i]));
        }
    }

}
