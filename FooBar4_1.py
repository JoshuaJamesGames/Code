#First a re-write of the problem
#Given a set of 3 lists:
#List of Entrances
#List of Exits
#List of Paths
#Numbers in Paths indicate the Bunny Flow Rate (BFR Hah!) between rooms
#in a given time cycle
#Find the largest number of bunnies that can escape in a time cycle through the
#paths

#First thoughts
#We are looking for bottlenecks in the paths
#Solve backwards from each exit finding the smallest BFR
#Sum up the exits

def solution(entrances, exits, path):
    # Your code here


#Tests template
#print(solution([],[],[]))
#Example 1: Answer is 16
print(solution([0,1],[4,5],
    [
        [0,0,4,6,0,0],
        [0,0,5,2,0,0],
        [0,0,0,0,4,4],
        [0,0,0,0,6,6],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0]

    ]))
#Example 2: Answer is 6
print(solution([0],[3],
    [
        [0,7,0,0],
        [0,0,6,0],
        [0,0,0,8],
        [9,0,0,0]
    ]))