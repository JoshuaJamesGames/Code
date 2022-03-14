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

def solution(map):
    # Your code here