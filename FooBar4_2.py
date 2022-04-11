#Restate the problem:
#Given a list of nodes with the cost (in time) to reach all other nodes (list of lists)
#The first node is the start, last node is the exit
#middle nodes in the list represent bunnies to be rescued with ID's incrementing from 0

#Also given a time limit, which bunnies can I save before (or as) time runs out
#Return them in an ordered list.  If the same number can be saved, prefer lists with
#lower ID #s

#Initial thoughts
#There are negative values in this directed graph
#I can rule out Dijktra's and subsequently A*
#I need to identify if there are time cycles
#If there are, then I can rescue all bunnies reachable from those loops

#Bellman-Ford seems like the algorithm of choice for path values
#and to identify cycles

#The wording "lowest ID #s" indicates I will be trying all combinations of
#bunnies

def solution(times, times_limit):
    # Your code here

#Sample 1 expected answer [1,2]
print(solution([
    [0, 2, 2, 2, -1], 
    [9, 0, 2, 2, -1], 
    [9, 3, 0, 2, -1], 
    [9, 3, 2, 0, -1], 
    [9, 3, 2, 2, 0]
],1))

#Sample 2 expected answer [0,1]
print(solution([
    [0, 1, 1, 1, 1], 
    [1, 0, 1, 1, 1], 
    [1, 1, 0, 1, 1], 
    [1, 1, 1, 0, 1], 
    [1, 1, 1, 1, 0]
],3))