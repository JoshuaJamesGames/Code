import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        String stringToTest;

        //Query for a line of text        
        System.out.println("Enter a phrase for the palindrome test.");
        stringToTest = scnr.nextLine();

        //Formatting for testing
        stringToTest = stringToTest.toLowerCase();
        stringToTest = stringToTest.replaceAll("[\\p{Punct}\\s]+", "");
        //Convert to an array in preparation for reversal

        char[] stringArray = stringToTest.toCharArray();
        char[] reverseStringArray = new char[stringToTest.length()];

        //Reverse the string
        for(int i=stringArray.length;i>0;i--){
            reverseStringArray[stringArray.length-i]=stringArray[i-1];
        }
        int isPalindrome = stringToTest.compareTo(String.valueOf(reverseStringArray));

        System.out.println("\"" + String.valueOf(reverseStringArray) + "\" is \"" + stringToTest + "\" reversed.");
        if(isPalindrome ==0){
            System.out.println("The input is a Palindrome");
        }
        else{
            System.out.println("The input is not a Palindrome");
        }
        scnr.close();
    }

}
