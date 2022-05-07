

/*
Develop a Java program that will store data in the form of daily average
temperatures for one week. Store the day and average temperature in two
different arraylists. Your program should prompt the user for the day 
of the week (Monday through Sunday) and display both the day and temperature
for each day. If "week" is entered, the output for your program should
provide the temperature for each day and the weekly average. 

Use the looping and decision constructs in combination with 
the arrays to complete this assignment.
*/

import java.util.Scanner;
import java.util.Random;
import java.util.ArrayList;


public class CSC320_CT5 {
    public static void main(String[] args) {
        ArrayList<String> daysOfWeek = new ArrayList<String>() {
            {
            add("Monday");
            add("Tuesday");
            add("Wednesday");
            add("Thursday");
            add("Friday");
            add("Saturday");
            add("Sunday");
            }
        };
        ArrayList<Double> dailyTemps = new ArrayList<Double>();
        Scanner scnr = new Scanner(System.in);
        String query = "";
        int queryIndex = -1;
        final int numTemps = daysOfWeek.size();

        setTemps(dailyTemps, numTemps);

        System.out.println("Welcome to the Weekly Temperature Program!");
        System.out.println("(Enter 'Monday'-'Sunday' for single days");
        System.out.println("'week' for a summary, or 'quit' to exit.");
        System.out.println("What temperature would you like no know?");

        query = scnr.next();

        while(!query.equals("quit")){
            
            if(query.equals("week")){

                printWeeklyTemps(dailyTemps, daysOfWeek);
                System.out.print("The weekly average temperature was: ");
                System.out.println(getAvgTemp(dailyTemps));

            }else if(daysOfWeek.contains(query)){

                queryIndex = daysOfWeek.indexOf(query);
                System.out.println("The temperature on " + query + " was: " 
                + dailyTemps.get(queryIndex));

            }else{

                System.out.println("I don't understand.");

            }

            System.out.print("What is your next query?: ");
            query = scnr.next();

        }
        scnr.close();
        System.out.println("\nGoodbye!\n");

    }

    public static void setTemps(ArrayList<Double> dailyTemps, int numTemps){
        Random rand = new Random();
        double randTemp;
        for(int i = 0; i < numTemps; i++){
            randTemp = Math.round(rand.nextDouble() * 10000.0) / 100.0;
            dailyTemps.set(i, randTemp); 
        }
    }

    
    public static void printWeeklyTemps(ArrayList<Double> dailyTemps, ArrayList<String> daysOfWeek){
        
        System.out.println("The daily temperatures were: ");
        for(int i = 0; i < daysOfWeek.size(); i++){
            
            System.out.println(daysOfWeek.get(i) + ": " + dailyTemps.get(i));
        }
    }

    public static double getAvgTemp(ArrayList<Double> dailyTemps){
        double sum = 0.0;
        for(int i = 0; i < dailyTemps.size(); i++){
            sum += dailyTemps.get(i);
        }
        return (Math.round((sum / dailyTemps.size()) * 100.0) / 100.0);
    }

}
