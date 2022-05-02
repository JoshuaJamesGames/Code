/*
CSC320-2 CTA3 - Option 1
Create a program that will calculate the weekly average tax withholding for a 
customer given the following weekly income guidelines:

Income less than $500: tax rate 10%
Incomes greater than/equal to $500 and less than $1500: tax rate 15%
Incomes greater than/equal to $1500 and less than $2500: tax rate 20%
Incomes greater than/equal to $2500: tax rate 30%.

*/
import java.util.Scanner;


public class CSC320_CT3 {
    public static void main(String[] args) {
        //Need to store Salary from user and calculate Tax with getTaxRate()
        double weeklySalary = 0.0;
        double taxRate = 0.0;
        Scanner scnr = new Scanner(System.in);
        //Prompt the user with an intro
        System.out.println("Welcome to the Tax Rate Calculator!");
        System.out.println("Enter your weekly income: ");        
        //Collect weekly salary info.  I am presuming perfect input 
        //since we haven't covered exceptions yet
        //Type conversion will occur if necessary
        weeklySalary = scnr.nextDouble();
        //taxRate is returned using weeklySalary
        taxRate = getTaxRate(weeklySalary);
        //output some stats for the user.
        showTaxStats(weeklySalary, taxRate);
        //Cleanup the scr and an outro
        scnr.close();
        System.out.println("Goodbye!\n");

    }
    
    public static double getTaxRate(double weeklySalary){
        double taxRate = 0.0;
        //taxRate is 0.0 if income is negative
        //An if else stack starting at the second range 
        
        if(weeklySalary >= 0 && weeklySalary < 500){
            taxRate = 0.10;
        }else if(weeklySalary >= 500 && weeklySalary < 1500){
            taxRate = 0.15;
        }else if(weeklySalary >= 1500 && weeklySalary < 2500){
            taxRate = 0.20;
        }else if(weeklySalary >= 2500){
            taxRate = 0.30;
        }
        //Return the taxRate
        return taxRate;
    }

    public static void showTaxStats(double weeklySalary, double taxRate){
        //Pre calculating some numbers to make formatting easier
        double weeklyTaxes = weeklySalary * taxRate;
        double weeklyIncome = weeklySalary - weeklyTaxes;
        //Added a moneySign for fun!
        char moneySign = '$';

        System.out.println("\nHere are some statistics: ");
        System.out.printf("With a %c%.2f weekly salary and a %.0f%% tax rate.\n", moneySign, weeklySalary, taxRate * 100);
        System.out.printf("You will pay %c%.2f in tax and keep %c%.2f per week.\n", moneySign, weeklyTaxes, moneySign, weeklyIncome);
        System.out.printf("You will pay %c%.2f in tax and keep %c%.2f every 4 weeks.\n", moneySign, weeklyTaxes * 4, moneySign, weeklyIncome * 4);
        System.out.printf("You will pay %c%.2f in tax and keep %c%.2f yearly.\n", moneySign, weeklyTaxes * 52, moneySign, weeklyIncome * 52);

    }

}
