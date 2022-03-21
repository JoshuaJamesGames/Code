#First, restate the problem
#We start with one of each bomb; M & F
#Each cycle we can either:
#Create M number of F bombs
#    or
#Create F number of M bombs
#Given a target of some number of both bombs x, y
#Return the number of cycles to reach that target 
#or 'impossible' if no combination can be found

#First thoughts...work in reverse from the target to x=1, y=1



def solution(x, y):
    # Your code here