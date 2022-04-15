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

#The wording "lowest ID #s" indicates I will be trying all permutations of
#bunnies

#I need permutations of the bunny ID #s
from itertools import permutations
from operator import neg

#From https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
def bellmanFord(graph, source):
    distances = [float('inf')] * len(graph)
    distances[source] = 0
    neg_cycles = False
   

    for each in range(len(distances)-1):
        for node in range(len(graph)):
            for destination in range(len(graph[node])):
                if distances[node] + graph[node][destination] < distances[destination]:
                    distances[destination] = distances[node] + graph[node][destination]

    for each in range(len(distances)-1):
        for node in range(len(graph)):
            for destination in range(len(graph[node])):
                if distances[node] + graph[node][destination] < distances[destination]:
                    distances[destination] = float('-inf')                  
    
    return distances


def getAllDistances(graph):
    
    distance_graph = []
    for node in range(len(graph)):
        distance_graph.append(bellmanFord(graph, node))
    return distance_graph

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

def get_rescue_times(path_times, bunny_permutations, times_limit):
    rescue_indexes = []
    for perm in bunny_permutations:
        travel_time = 0
        travel_time += path_times[0][perm[0]]
        for index in range(len(perm)-1):
            travel_time += path_times[perm[index]][perm[index+1]]
        travel_time += path_times[perm[-1]][-1]
        if travel_time <= times_limit:
            rescue_indexes.append(sorted(perm))
    return rescue_indexes



def solution(times, times_limit):
    num_bunnies = len(times)-2
    bunny_indexes = [x for x in range(1,num_bunnies+1)]
    best_rescue_indexes = []
    best_rescue = []

    path_times = getAllDistances(times)
    print(path_times)       

    for num in range(1, num_bunnies + 1):
        bunny_permutations = list(permutations(bunny_indexes, num))
        rescue_indexes = get_rescue_times(path_times, bunny_permutations, times_limit)
        if len(rescue_indexes) > 0:
            best_rescue_indexes = sorted(rescue_indexes)
            break
    #print(best_rescue_indexes)
    if len(best_rescue_indexes) > 0: 
        best_rescue = best_rescue_indexes[0]
        best_rescue = [x-1 for x in best_rescue]
        #print(best_rescue)
    return best_rescue

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

#Sample 3 has a negative cycle
print(solution([
    [0, 1, 1, 1, 1, 1], 
    [1, 0, 1, 1, 1, 1], 
    [1, 1, 0, 1, 1, 1], 
    [1, 1, 1, 0, 1, 1], 
    [1, 1, 1, 1, 0, -1],
    [1, 1, 1, 1, -1, 0]
],0))

#Trying a max_bunny size graph
print(solution([
    [0, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 1, 1, 1, 1], 
    [1, 1, 0, 1, 1, 1, 1], 
    [1, 1, 1, 0, 1, 1, 1], 
    [1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0]
],6))

#What if there are 0 bunnies
print(solution([
    [0, 1],      
    [1, 0]
],0))