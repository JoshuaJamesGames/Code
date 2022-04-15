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
#Check nearness first - might be a small matrix (2x2)
import copy

#Stay within bounds while navigating
def within_bounds(node, map):
    (row,column) = node
    if row < 0 or column < 0 or row > len(map)-1 or column > len(map[0])-1:
        return False
    else:
        return True

#I used a tuple instead of a dictionary...so here is my solution
def is_visited(row, column, path): 
    visited = False   
    for index in range(len(path)):
        (check_row, check_column) = (path[index][0],path[index][1])
        #print(len(path), row, node[0], column, node[1])
        if row == check_row and column == check_column:
            #print('Been there',row, node[0], column, node[1])
            visited = True
        
    return visited

#Adding weighted travel based on distance to target and dimensions of maze
def get_steps(path, map):
    weight_list =[]
    origin = path[0]
    last_step = path[len(path) - 1]
    height = len(map)
    width = len(map[0])
    destination = (height - origin[0], width - origin[1])

    up_weight = (last_step[0] - destination[0] , (-1,0))
    weight_list.append(up_weight)
    down_wieght = (destination[0] - last_step[0], (1,0))
    weight_list.append(down_wieght)
    left_weight = (last_step[1] - destination[1], (0,-1))
    weight_list.append(left_weight)
    right_weight = (destination[1] - last_step[1], (0,1))
    weight_list.append(right_weight)

    weight_list = sorted(weight_list, key = lambda weight: weight[0], reverse=True)

    steps = []
    for step in weight_list:
        steps.append(step[1])
    return steps

def find_the_distance(start, map, destination):
    path_traveled =[start]
    nodes_to_visit = [start]
    destination_reached = False
    while nodes_to_visit and not destination_reached:
        current_node = nodes_to_visit.pop(0)
        steps = get_steps(path_traveled, map)
        for step in steps:
            (step_row,step_column) = step
            (row, column, distance) = current_node
            new_row = row + step_row
            new_column = column + step_column
            if not within_bounds((new_row,new_column), map):
                continue
            if not is_visited(new_row, new_column, path_traveled) and map[new_row][new_column] != 1:
                path_traveled.append((new_row, new_column, distance+1))
                nodes_to_visit.append((new_row, new_column, distance+1))
                if is_visited(destination[0],destination[1],path_traveled):
                    destination_reached = path_traveled[len(path_traveled)-1][2]
                
    return destination_reached


def solution(map):
    origin_node = (0,0,1) #(row,column,distance)
    destination_node = (len(map)-1,len(map[0])-1, 1) #(row,column,distance)
    shortest_distance = len(map) + len(map[0]) -1 #This is the minimum with 1 wall
    max_distance = 201    
    distance = max_distance
    for row in range(len(map)):
        for column in range(len(map[row])):
            if map[row][column] == 1: #I could leave this off, but no
                copy_map = copy.deepcopy(map)                
                copy_map[row][column] = 0
                if find_the_distance(origin_node,copy_map,(row,column)) and find_the_distance(destination_node, copy_map, (row,column)):
                    new_distance = find_the_distance(origin_node,copy_map,(row,column)) + find_the_distance(destination_node, copy_map, (row,column)) -1
                    #print(find_the_distance(origin_node,copy_map,(row,column)), find_the_distance(destination_node, copy_map, (row,column)), (row,column))
                    if new_distance == shortest_distance:
                        return new_distance
                    else: 
                        #print(distance, new_distance)
                        distance = min(distance, new_distance)
    return distance

    
    #return find_the_distance(origin_node, map, destination_node)

example1 = [
    [0,1,1,0],
    [0,0,0,1],
    [1,1,0,0],
    [1,1,1,0]
    ]
print(solution(example1))

example2 = [
    [0,0,0,0,0,0],
    [1,1,1,1,1,0],
    [0,0,0,0,0,0],
    [0,1,1,1,1,1],
    [0,1,1,1,1,1],
    [0,0,0,0,0,0]
    ]
print(solution(example2))

example3 = [
    [0,1],
    [0,0]
    ]
print(solution(example3))

example4 = [
    [0,0,0,1,0,0],
    [0,1,1,1,0,0],
    [0,1,0,0,0,0],
    [0,0,0,1,0,1],
    [1,0,0,1,0,0]
    ]
print(solution(example4))

example5 = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,1,1],
    [0,0,1,0]
]
print(solution(example5))

example6 = [
    [0,0,0,0,0],
    [1,0,1,1,0],
    [0,0,1,1,0],
    [0,1,1,0,1],
    [0,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,0]
    ]
print(solution(example6))