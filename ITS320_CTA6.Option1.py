#For this assignment, you are given two complex numbers. You will print the 
# result of their addition, subtraction, multiplication, division, and 
# modulus operations. The real and imaginary precision part should be correct 
# up to two decimal places.

#Input Format
#One line of input: The real and imaginary part of a number separated by a space.

#Output Format
#For two complex numbers and the output should be in the following sequence 
# on separate lines:

#C + D
#C - D
#C * D
#C / D
#mod(C)
#mod(D)

#For complex numbers with non-zero real and complex part, the output should be in the following format: 
#A + Bi

#Replace the plus symbol (+) with a minus symbol (-) when B 0.
#For complex numbers with a zero complex part, i.e. real numbers, the output should be: 
#A + 0.00i

#For complex numbers where the real part is zero and the complex part is non-zero, the output should be:
#0.00 + Bi

#Sample Input
#2 1
#5 6

#Sample Output
#7.00+7.00i
#-3.00-5.00i
#4.00+17.00i
#0.26-0.11i
#2.24+0.00i
#7.81+0.00i

import math

class Complex(object):
    def __init__(self, real=0, imaginary=0):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __add__(self, no):
        # enter your code here
        return Complex(real, imaginary)

    def __sub__(self, no):
        # enter your code here       
        return Complex(real, imaginary)

    def __mul__(self, no):
        # enter your code here
        return Complex(real, imaginary)

    def __truediv__(self, no):
        # enter your code here
        return Complex(real, imaginary)

    def mod(self):
        # enter your code here
        return Complex(real, 0)

    def __str__(self):
        # enter your code here
        return result

# put this code in a main method
C = map(float, input().split())
D = map(float, input().split())
x = Complex(*C)
y = Complex(*D)
print ('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))) 