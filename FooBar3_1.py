

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

#Multiplication : Input matrices need to match : matrix1 columns == matrix2 rows
#Not going to do error checking as my input should be valid
def mult_matrix(matrix1,matrix2):
    answer = []
    for column in range(len(matrix2[0])):
        answer.append([])        
        for row in range(len(matrix1)):
            sum=0
            for subrow in range(len(matrix1[0])):                
                sum += matrix1[row][subrow] * matrix2[subrow][column]          
            answer[column].append(sum)
    return answer

#Holy crap inverting a matrix!  Credit to https://github.com/ThomIves/MatrixInverse/blob/master/MatrixInversion.py
#I originally found it at https://integratedmlai.com/matrixinverse/
#Thank goodness we have written programs to do this
def zeros_matrix(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
        :returns: list of lists that form the matrix.
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M
def identity_matrix(n):
    """
    Creates and returns an identity matrix.
        :param n: the square size of the matrix
        :returns: a square identity matrix
    """
    I = zeros_matrix(n, n)
    for i in range(n):
        I[i][i] = 1.0

    return I
def copy_matrix(M):
    """
    Creates and returns a copy of a matrix.
        :param M: The matrix to be copied
        :return: The copy of the given matrix
    """
    rows = len(M)
    cols = len(M[0])

    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(rows):
            MC[i][j] = M[i][j]

    return MC
def invert_matrix(A, tol=None):
    """
    Returns the inverse of the passed in matrix.
        :param A: The matrix to be inversed
        :return: The inverse of the matrix A
    """
   
    #Make copies of A & I, AM & IM, to use for row operations
    n = len(A)
    AM = copy_matrix(A)
    I = identity_matrix(n)
    IM = copy_matrix(I)

    #Perform row operations
    indices = list(range(n)) # to allow flexible row referencing ***
    for fd in range(n): # fd stands for focus diagonal
        fdScaler = 1.0 / AM[fd][fd]
        # FIRST: scale fd row with fd inverse. 
        for j in range(n): # Use j to indicate column looping.
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        # SECOND: operate on all rows except fd row as follows:
        for i in indices[0:fd] + indices[fd+1:]: # *** skip row with fd in it.
            crScaler = AM[i][fd] # cr stands for "current row".
            for j in range(n): # cr - crScaler * fdRow, but one element at a time.
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    #Converting to Fractions : This is not in the original
    for row in range(n):
        for column in range(n):
            IM[row][column] = Fraction(IM[row][column]).limit_denominator()
    return IM

def solution(m):
    print('Q is:')
    printMatrix(getQ(m))
    print()

    print('R is:')
    printMatrix(getR(m))
    print()

    print('I is:')
    printMatrix(getI(m))
    print()

    print('I-Q is:')    
    printMatrix(sub_matrix(getI(m),getQ(m)))
    print()

    print('Inverse of (I-Q) is:')
    printMatrix(invert_matrix(sub_matrix(getI(m),getQ(m))))
    print()

    print('The inverse of (I-Q) *R is:')
    
    
    

#Example 1
#print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))

#Example 2
#print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))

#Example 3 from Brilliant.org
print(solution([[0,1,0,1,0],[1,0,1,0,0],[0,1,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]))