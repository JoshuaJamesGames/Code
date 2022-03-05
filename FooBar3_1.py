

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



def solution(m)


print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))