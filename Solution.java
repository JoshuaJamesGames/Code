/*
Re-write of the problem.
Given a string (s) representation of an integer (up to 10**100)
Calculate the sum of the seqence 1-s where each number (s) is the floor(s*sqrt(2))
-floor(1*sqrt(2))+floor(2*sqrt(2))+floor(3*sqrt(2))...

example 1:
Solution.solution('5'); 
1 + 2 + 4 + 5 + 7
returns 19

example 2:
Solution.solution('77');
1 +2 + 4 + 5 + 7...108
returns 4208

Because of the size of input, we can't use a loop
Formula is derived from the base series 1-n
n*(n+1)/2

The given sequence (floor(n*sqrt(2))) is a Beatty sequence so it has a complementary sequence (floor(n*(2+sqrt(2)))).
The Beatty and its Complementary sequence partition all natural numbers

So we need to subtract the compliment from the base...sounds so simple
We need precision...so using BigDecimal

SqrtOfTwo = "1.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727"
N = s
C = Compliment of N = floor((SqrtOfTwo-1)*N)

Final formula is recursive: 

    Series(N):

    if N = 0 return 0
    
    return N*C + N(N+1)/2 - C(C+1)/2 - Series(C)

I would like to thank the mathematicians that came before me...and the internet
https://oeis.org/A001951/internal
https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html
https://en.wikipedia.org/wiki/Square_root_of_2
https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s/2053713#2053713
https://en.wikipedia.org/wiki/Recurrence_relation#Solving
https://catonmat.net/tools/generate-sqrt2-digits

*/

import java.math.BigDecimal;
//import java.math.MathContext;
import java.math.RoundingMode;

public class Solution {

    String SqrtOfTwoString = "1.4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727";
    BigDecimal SqrtOfTwo = new BigDecimal(SqrtOfTwoString);

    public static int BeattySeries(BigDecimal SqrtOfTwo, int N){
        BigDecimal CminusOne = SqrtOfTwo.subtract(new BigDecimal("1"));
        BigDecimal CminusOneMultiplied = CminusOne.multiply(new BigDecimal(N));
        BigDecimal BigC = CminusOneMultiplied.setScale(0,RoundingMode.FLOOR);
        int C = BigC.intValue();

        if(N == 0){
            return 0;
        }

        return (N*C) + (N*(N+1)/2) - (C*(C+1)/2) - BeattySeries(SqrtOfTwo, C);
    }

    public String solution(String s){

        int N = Integer.parseInt(s);

        int series = BeattySeries(SqrtOfTwo, N);

        return Integer.toString(series);
    }

    


public static void main(String[] args) {
    Solution test = new Solution();
    System.out.println(test.solution("77"));

}
}