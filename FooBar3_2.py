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

#Nearly there distance
#How many steps from one node to another
nearly_there = 2

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

#Check to see if the nodes are within one (1) distance of each other
def within_one(origin_path, destination_path):
    #reference the last node on origin list vs the destination path 
    origin_node = origin_path[-1]
    (origin_row, origin_column) = origin_node[0:2]
    for destination_node in destination_path:
        (destination_row, destination_column) = destination_node[0:2]
        if abs(origin_row - destination_row) + abs(origin_column - destination_column) <= nearly_there:
            return origin_node, destination_node
        
    #Reference the last node on the destination list vs origin path
    destination_node = destination_path[-1]
    (destination_row, destination_column) = destination_node[0:2]
    for origin_node in origin_path:
        (origin_row, origin_column) = origin_node[0:2]
        if abs(origin_row - destination_row) + abs(origin_column - destination_column) <= nearly_there:
            return origin_node, destination_node
        
    return False
#Adding weighted travel based on distance to target and dimensions of maze
def get_steps(path,map):
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


    
def get_next_node(path, queue, map):
    
    steps = get_steps(path, map)
    if queue:
        for step in steps:
            (step_row,step_column) = step
            (row, column, distance) = queue[0]
            new_row = row + step_row
            new_column = column + step_column
            if not within_bounds((new_row,new_column), map):
                continue
            if not is_visited(new_row, new_column, path) and map[new_row][new_column] != 1:
                #print(is_visited(new_row, new_column, path))
                path.append((new_row, new_column, distance+1))
                queue.append((new_row, new_column, distance+1))
                #print('Queue:',queue)
                #print('Path:', path)

        next_node = queue.pop(0)
    #path.append(next_node)
    
    return 

def navigate(origin_path, origin_queue, destination_path, destination_queue, map):
    path_found = within_one(origin_path, destination_path)
    
    while not (path_found):

        get_next_node(origin_path, origin_queue, map)
        found_from_origin = within_one(origin_path, destination_path)

        get_next_node(destination_path, destination_queue, map)
        found_from_destination = within_one(origin_path, destination_path)

        if found_from_origin or found_from_destination:
            path_found = within_one(origin_path, destination_path)
    #print('Path found: ', path_found[0],path_found[1])
    return path_found[0][2] + path_found[1][2] +1


def solution(map):
    origin_path = [(0,0,1)] #(row,column,distance)
    destination_path = [(len(map)-1,len(map[0])-1, 1)] #(row,column,distance)
    origin_queue = origin_path[:]
    destination_queue = destination_path[:]
    #print(origin_queue, destination_queue)
    return navigate(origin_path, origin_queue, destination_path, destination_queue, map)

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
    [0,0],
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
    [0,0,0,1,0]
    ]
print(solution(example6))