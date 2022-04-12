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

#I need permutations of the bunny ID #s
from itertools import permutations

#From https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
def bellmanFord(graph, source):
    distances = [float('inf')] * len(graph)
    distances[source] = 0
   

    for each in range(len(distances)-1):
        for node in range(len(graph)):
            for destination in range(len(graph[node])):
                if distances[node] + graph[node][destination] < distances[destination]:
                    distances[destination] = distances[node] + graph[node][destination]

    return distances
#This was a great learning experience...but I need permutations not combinations
def bunnyCombinations(bunny_list, combo_length):
    if combo_length == 0:
        return [[]]
     
    combo_list =[]
    for index in range(len(bunny_list)):
         
        m = bunny_list[index]
        remLst = bunny_list[index + 1:]
         
        for piece in bunnyCombinations(remLst, combo_length-1):
            combo_list.append([m]+piece)
             
    return combo_list


def solution(times, times_limit):
    num_bunnies = len(times)-2
    bunny_indexes = [x for x in range(1,num_bunnies+1)]

    print(bellmanFord(times, 0))
    
    print(list(permutations(bunny_indexes)))
    pass

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

print(solution([
    [0, 1, 1, 1, 1, 1], 
    [1, 0, 1, 1, 1, 1], 
    [1, 1, 0, 1, 1, 1], 
    [1, 1, 1, 0, 1, 1], 
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0]
],4))