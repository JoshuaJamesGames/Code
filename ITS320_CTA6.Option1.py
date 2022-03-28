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
    def __init__(self, real=0, imaginary=0): #Adding defaults of 0 in case only 1 number is provided
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no): #Overriding the addition operator
        real = self.real + no.real
        imaginary = self.imaginary + no.imaginary
        return Complex(real, imaginary)

    def __sub__(self, no): #Overriding the subtraction operator
        real = self.real - no.real
        imaginary = self.imaginary - no.imaginary      
        return Complex(real, imaginary)

    def __mul__(self, no): #Overriding the Multiplication operator
        real = ((self.real * no.real) - (self.imaginary * no.imaginary))
        imaginary = ((self.imaginary * no.real) + (self.real * no.imaginary))
        return Complex(real, imaginary)

    def __truediv__(self, no): #Overriding the Division Operator
        real = ((self.real * no.real) + (self.imaginary * no.imaginary)) / (no.real**2 + no.imaginary**2)
        imaginary = ((self.imaginary * no.real) - (self.real * no.imaginary)) / (no.real**2 + no.imaginary**2)
        return Complex(real, imaginary)

    def mod(self): #Overriding the Modulus Operator
        real = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(real, 0)

    def __str__(self): #Overriding __str__ to enable proper printing (.2f) for 2 decimal places
        real_string = f'{self.real:.2f}'
        if self.imaginary < 0:
            imaginary_string = f'{self.imaginary:.2f}'
        else:
            imaginary_string = f'+{self.imaginary:.2f}'
        return real_string+imaginary_string+'i'

def main():
    #Some output to get the user ready to input some strings
    print('This program will ask you for two pairs of numbers.')
    print('Each pair represents a complex number such as "A + Bi"')
    print('The numbers should be input separated by a space. Ex: 2 1')
    print('Once both have been collected it will output a series of six operations')
    print('Addition, subtraction, multiplication, division, and separate modulus.')
    print('Each on their own line.\n')

    #Collect input from the user with 2 prompts instead of a loop because
    #the assignment contains mandatory code usage.
    #Req: put this code in a main method

    #map() returns a list floats from the input after splitting
    C = map(float, input('What is the first pair of numbers: ').split())
    D = map(float, input('What is the second pair of numbers: ').split())
    
    #In this instance the * operator is creating a tuple for the variables to intantiate 2 Complex objects
    x = Complex(*C)
    y = Complex(*D)

    #Here we are using join()-ing the results of a series of operations that are turned
    #into strings, output as a list, and '\n' (new-lines) are appended between them to achieve the 
    #desired output format
    print() 
    print ('\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))) 

if __name__=='__main__':
    main()