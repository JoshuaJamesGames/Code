import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        int firstNum;
        int secondNum;
        System.out.println("What is the first number?");
        firstNum = scnr.nextInt();
        System.out.println("What is the second number?");
        secondNum = scnr.nextInt();
        System.out.println(firstNum + " + " + secondNum + " = " + (firstNum + secondNum));
        System.out.println(firstNum + " - " + secondNum + " = " + (firstNum - secondNum));
        System.out.println(firstNum + " x " + secondNum + " = " + (firstNum * secondNum));
        System.out.println(firstNum + " / " + secondNum + " = " + (firstNum / secondNum));
        scnr.close();
    }

}
