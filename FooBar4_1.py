#First a re-write of the problem
#Given a set of 3 lists:
#List of Entrances
#List of Exits
#List of Paths
#Numbers in Paths indicate the Bunny Flow Rate (BFR Hah!) between rooms
#in a given time cycle
#Find the largest number of bunnies that can escape in a time cycle through the
#paths
#Max of 50 paths and 2,000,000+1 flow rate
#Exits can't be entrances

#First thoughts
#We are looking for bottlenecks in the paths
#Sum up the min from each path

#Update - learned about Ford-Fulkerson algorithm

#I learned what an adjancency matrix is - I need a class because to keep
#track of the Graph data accross multiple iterations of ford_fulkerson
class Graph:
    def __init__(self, graph):
        self.graph = graph  # This graph will be updated until it can't be        
        self.ROW = len(graph)
    def bfs(self, source, target, parent):

        #Create Queues for visited and to visit
        visited = []
        queue = []

        #Mark the source node as visited and enqueue it
        queue.append(source)
        visited.append(source)

        #Hey it's BFS again
        while queue:
            
            current = queue.pop(0)

            for index, value in enumerate(self.graph[current]):
                if index not in visited and value > 0:
                    queue.append(index)
                    visited.append(index)
                    parent[index]= current
                    print(parent)

        if target in visited:
            return True
        else: 
            return False

    #Returns the maximum flow from source to sink in the given graph
    #From https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
    def ford_fulkerson(self, source, sink):

        #This array is filled by BFS and to store path
        #Initialized to 0
        parent = [0] * self.ROW

        max_flow = 0  #There is no flow initially

        #Keep searching until we can't find a path
        #Either there isn't one or we have used all the capacity
        while self.bfs(source, sink, parent):
            print(self.graph)
            #Find the minimum along the path created by bfs()
            #It will be the max_flow because of restriction
            min_flow = 2000001 #Max from the challenge readme.txt
            s = sink
            while s != source:                
                min_flow = min(min_flow, self.graph[parent[s]][s])
                s = parent[s]

            #Add min_flow to overall flow
            max_flow += min_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= min_flow
                self.graph[v][u] += min_flow
                v = parent[v]
            print(self.graph)
        return max_flow

def solution(entrances, exits, path):
    corridors = Graph(path)
    max_bunny_flow = 0
    for entrance in entrances:
        for exit in exits:
            max_bunny_flow += corridors.ford_fulkerson(entrance, exit)
    return max_bunny_flow

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