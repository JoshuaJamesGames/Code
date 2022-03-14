#First, a rewrite of the problem
#Input will be a matix of 0s or 1s representing passable nodes
#Start is top-left (0,0)
#End is bottom-right (width-1, height-1)
#Find the shortest path between them
#I can remove one (1) wall
#Return the number of nodes traversed including the start & end
#No diagonal moves and matrix will be from 2-20 in width or height

#Thoughts
#Minimum path will be width + height -1
#Perform a depth first search from both ends weighing navigation 
#   Positive from origin
#   Negative from destination
#If paths come within one (1) distance of each other - found the path
#Check nearness first - might be a small matrix (2x2)

#Stay within bounds while navigating
def within_bounds(node, map):
    row,column = node
    if row < 0 or column < 0 or row > len(map)-1 or column > len(map[0])-1:
        return False
    else:
        return True

#Check to see if the nodes are within one (1) distance of each other
def within_one(origin_node, destination_node):


def navigate(origin_path, destination_path):



def solution(map):
    origin_path = [(0,0)]
    destination_path = [(len(map)-1,len(map[0])-1)]
    print(origin_path,destination_path)

    return #Distance

example1 = [[0,1,1,0],[0,0,0,1],[1,1,0,0],[1,1,1,0]]
solution(example1)

example2 = [[0,0,0,0,0,0],[1,1,1,1,1,0],[0,0,0,0,0,0],[0,1,1,1,1,1],[0,1,1,1,1,1],[0,0,0,0,0,0]]
solution(example2)