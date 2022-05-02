/*
Write a program that will provide important statistics for the grades in a class. 
The program will utilize a for-loop to read ten floating-point grades from user 
input. Include code to prevent an endless loop. Ask the user to enter the values, 
then print the following data:

Average
Maximum
Minimum

*/
//Need input and will store the values in an array;
import java.util.Scanner;
import java.util.Arrays;

public class CSC320_CT4 {
    public static void main(String Args[]){
        
        //Intro to the program and very brief directions
        System.out.println("Welcome to the Class Grades Statistics Program!");
        System.out.println("You will enter 10(ten) grades in decimal format ex: 88.5");

        //Initialize a class Class - dancing on the border of a reserved word 
        Class students = new Class();

        //Just a space for formatting
        System.out.println();

        //Output the required fields
        students.printAvg();
        students.printMax();
        students.printMin();

        //Make sure the user knows we are done
        System.out.println("\nGoodbye!\n");
        

    }
    //Class will store 10 grades and output Average/Max/Min grade
    public static class Class{
        //I need the array for easy computation and storage
        private double[] grades = new double [10];

        //These 3 are perhaps unecessary as the value could be computed
        //but I like them for readability
        private double averageGrade = 0;
        private double minGrade = 0;
        private double maxGrade = 0;

        //Need input from user
        Scanner scnr = new Scanner(System.in); 

        //Constructor will query the user for 10 numbers
        //storing as doubles - Once again expecting perfect input
        public Class(){
            for(int i = 0; i < 10; i++){
                System.out.print("Enter grade #"+ (i+1) +": ");
                grades[i] = scnr.nextDouble();
            }
            //Sort the array to pull min/max easily
            Arrays.sort(grades);
            averageGrade = computeAvg();
            minGrade = grades[0];
            maxGrade = grades[9];
            
        }
        //Loops through the grades :returns the sum divided by 10
        private double computeAvg(){
            double sum = 0.0;
            for(int i = 0; i< 10; i++){
                sum += grades[i];
            }
            return sum / 10;
        }
        //Good method names are self-commenting
        public void printAvg(){
            System.out.println("The Average grade is: " + averageGrade);
        }
        public void printMax(){
            System.out.println("The Maximum grade is: " + maxGrade);
        }
        public void printMin(){
            System.out.println("The Minimum grade is: " + minGrade);
        }
    }

}

