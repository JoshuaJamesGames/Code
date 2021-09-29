import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        String stringToTest;

        //Query for a line of text        
        System.out.println("Enter a phrase for the palindrome test.");
        stringToTest = scnr.nextLine();

        //Convert to an array in preparation for reversal
        char[] stringArray = stringToTest.toCharArray();
        char[] reverseStringArray = new char[stringToTest.length()];

        //Reverse the string
        for(int i=stringArray.length;i>0;i--){
            reverseStringArray[stringArray.length-i]=stringArray[i-1];
        }

        System.out.println("\"" + String.valueOf(reverseStringArray) + "\" is \"" + stringToTest + "\" reversed.");
        scnr.close();
    }

}
