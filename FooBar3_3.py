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

def regress(mach, facula):
    if mach - facula <=0 and facula - mach <=0: #If we can't take another cycle
        return 'impossible'
    elif mach - facula == mach or facula - mach == facula: #If the number equal each other
        return 'impossible'
    elif mach - facula <=0:
        if facula // mach > 1: #If there is a multiple step we can take, but not all the way to zero
            return (mach, facula - mach * ((facula // mach)) + mach, (facula // mach)-1)
        else:
            return (mach, facula - mach, 1)
    else:
        if mach // facula > 1:
            return(mach - facula * ((mach // facula))+ facula, facula, (mach // facula)-1)
        else:
            return (mach - facula, facula, 1)



def solution(x, y):
    cycles = 0 #Base case if (x, y) == (1, 1)
    #Better names
    mach = int(x)
    facula = int(y)
    #Base Case
    if (mach, facula) == (1, 1):
        return str(cycles)
    
    while regress(mach, facula) != 'impossible' and (mach, facula) != (1, 1):
    
        (mach, facula, steps) = regress(mach, facula)
        cycles += steps #Extract the steps and append
        
    if (mach, facula) != (1, 1) and regress(mach, facula) == 'impossible': #We can't reach (1,1)
        return 'impossible'
    else:
        return str(cycles)

    
print(solution(1,1))

print(solution(2,1))

print(solution(4,7))

print(solution(3,3))

print(solution(1,2))