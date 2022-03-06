

#Ok...We are given a matrix with absorbing states
#The initial state is m[0] and I need to return the chances of
#ending at an absorbing state as fractions, but in the form of
#[Numerator, Numerator...,Denominator] for all absorbing states

#We are dealing with an absorbing Markov Chain
#From Wikipedia and Brilliant.org
#The Fundamental matrix can be found as N = (I-Q)^-1
#The Absorbing Probability matrix is B = N*R
#So I need the first row of B = ((I-Q)^-1)* R

#Q = Transition x Transixion Matrix
#R = Transition x Absorbent Matrix
#I = Absorbent identity Matrix

#No Matrix operations in Python 2.7 so...
#Going to need a Least Common Denominator for fractions
from fractions import Fraction

#I want to see progress as I proceed
def printMatrix(matrix):
    for row in matrix:
        print(row)

#Going to need a list of the Non-Absorbent or the opposite
def getAbsorbents(matrix):
    absorbents = []
    for row in matrix:
        if sum(row)==0: #If all 0's
            absorbents.append(True)
        else:
            absorbents.append(False) #Might come back and insert the sum for fractions
    return absorbents

#Let's get Q first
def getQ(matrix):
    absorbents = getAbsorbents(matrix)    
    matrixQ =[]
    for row in range(len(matrix)):
        if absorbents[row] != True:
            matrixQ.append([])
            for column in range(len(matrix[row])):
                if absorbents[column] != True:
                    if matrix[row][column]==0:
                        matrixQ[row].append(0)
                    else:
                        matrixQ[row].append(Fraction(matrix[row][column],sum(matrix[row]))) #Yay! Fraction again
    return matrixQ

#Now we can get R
def getR(matrix):
    absorbents = getAbsorbents(matrix)    
    matrixR =[]
    for row in range(len(matrix)):
        if absorbents[row] != True:
            matrixR.append([])
            for column in range(len(matrix[row])):
                if absorbents[column] == True:
                    if matrix[row][column]==0:
                        matrixR[row].append(0)
                    else:
                        matrixR[row].append(Fraction(matrix[row][column],sum(matrix[row])))                   
    return matrixR

def solution(m):
    print('Q is:')
    printMatrix(getQ(m))
    print('R is:')
    printMatrix(getR(m))
    

#Example 1
print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))

#Example 2
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))