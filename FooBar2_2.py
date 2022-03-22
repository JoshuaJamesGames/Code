#Rewording the problem:
#Given a perfect binary tree of height h and,
#a list of integers q
#return a list of the parent or root nodes values above the given integers
#or -1 if the integer is the top of the tree

#Perfect tree will be (2**h)-1 nodes
#Each level has (2**h)-1 nodes, which is also the root of each branch
#Feels like a binary search
#Each level will accumulate (powers of 2)-1 if they are greater

def solution(h, q):
    #Better variable names
    height = h
    sub_nodes = q
    parent_nodes = []
    root = (2**height)-1
    
    child = 0
    parent = 0
    #Iterate throught the sub_nodes
    for node in sub_nodes:
        #First case: is it root?
        if node == root: #This is the root
            parent_nodes.append(-1)
            print('This is root, appended -1')
        else:
            print(node)
            accumulator =0
            parent = root
            for level_from_top in range(1,height+1):
                if node == child: #Found it and break inner loop
                    parent_nodes.append(parent)
                    print(parent, 'appended')
                    break
                if node <= 2**(height - (level_from_top))-1+accumulator:
                    #print((2**(height - (level_from_top)))-1)
                    child = 2**(height - (level_from_top))-1+accumulator
                    parent = 2**(height - (level_from_top -1))-1+accumulator
                    print('left',parent,child,node)
                else:
                    parent = 2**(height - (level_from_top -1))-1+accumulator
                    accumulator += 2**(height - (level_from_top))-1
                    child = 2**(height - (level_from_top))-1+accumulator
                    print('right',parent,child,node)
                
    return parent_nodes
print(solution(5,[19, 14, 28]))
#21,15,29
print(solution(3, [7, 3, 5, 1]))
#-1,7,6,3