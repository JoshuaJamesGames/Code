

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
from re import sub

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

#Let's get Q first : The Transition x Transition Matrix
def getQ(matrix):
    absorbents = getAbsorbents(matrix)    
    matrixQ =[]
    num_rows = 0
    for row in range(len(matrix)):
        if absorbents[row] != True:
            matrixQ.append([])
            num_rows += 1
            for column in range(len(matrix[row])):
                if absorbents[column] != True:
                    if matrix[row][column]==0:
                        matrixQ[num_rows-1].append(0)
                    else:
                        matrixQ[num_rows-1].append(Fraction(matrix[row][column],sum(matrix[row]))) #Yay! Fraction again
    return matrixQ

#Now we can get R : The Transition X Absorbing Matrix
def getR(matrix):
    absorbents = getAbsorbents(matrix)    
    matrixR =[]
    num_rows = 0
    for row in range(len(matrix)):
        if absorbents[row] != True:
            matrixR.append([])
            num_rows += 1
            for column in range(len(matrix[row])):
                if absorbents[column] == True:
                    if matrix[row][column]==0:
                        matrixR[num_rows-1].append(0)
                    else:
                        matrixR[num_rows-1].append(Fraction(matrix[row][column],sum(matrix[row])))                   
    return matrixR

#And now I : The identity matrix of non-absorbents
def getI(matrix):
    absorbents = getAbsorbents(matrix)
    matrixI = []
    num_rows = 0    
    for row in range(len(matrix)):
        if absorbents[row] != True:
            matrixI.append([])
            num_rows += 1
            for column in range(len(matrix[row])):
                if absorbents[column] != True:
                    if row==column:
                        matrixI[num_rows-1].append(1)
                    else:
                        matrixI[num_rows-1].append(0)

    return matrixI

#Going to need some matrix operations
#We'll go Subtraction first
def sub_matrix(matrix1,matrix2):
    answer = []
    for row in range(len(matrix1)):
        answer.append([])
        for column in range(len(matrix1[row])):
            answer[row].append(matrix1[row][column]-matrix2[row][column])
    return answer

#Multiplication
def mult_matrix(matrix1,matrix2):
    answer = []
    for column in range(len(matrix2[0])):
        answer.append([])        
        for row in range(len(matrix1)):
            sum=0
            for subrow in range(len(matrix1[0])):                
                sum += matrix1[row][subrow] * matrix2[subrow][column]
                print(matrix1[row][subrow], matrix2[subrow][column])
            print('appended')
            answer[column].append(sum)
    return answer

def solution(m):
    print('Q is:')
    printMatrix(getQ(m))
    print('R is:')
    printMatrix(getR(m))
    print('I is:')
    printMatrix(getI(m))
    print('I-Q is:')    
    printMatrix(sub_matrix(getI(m),getQ(m)))
    printMatrix(mult_matrix([[1,7],[2,4]],[[3,3],[5,2]]))
    test1= [[2,4],[-1,-2],[7,-12]]
    test2= [[5],[-3]]
    printMatrix(mult_matrix(test1,test2))
    

#Example 1
#print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))

#Example 2
#print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))

#Example 3 from Brilliant.org
print(solution([[0,1,0,1,0],[1,0,1,0,0],[0,1,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]))