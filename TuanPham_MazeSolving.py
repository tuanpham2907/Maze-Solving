import sys

"""
 * Maze Solver Problem
 * @author Tuan Pham
 *
"""


print('********************  Maze Solving ********************')

filename = input("Enter maze file: ")

try:
    with open(filename,'r') as f:
        content = f.readlines()
except:
    print("File not found! Please enter a valid file name!!!")
    sys.exit()

print('********************  The original Maze ********************')


# take the first two int as number of row and column
helper = content.pop(0).replace("\n",'').split(' ')
row = int(helper[0])
col = int(helper[1])


# print the original maze
for element in content:
    element = element.strip('\n')
    print(element)

print('\n')
print('************************  Maze Solved ************************')


solveMaze = [[0 for i in range(0,col)] for j in range(row)]

# convert maze to an 2-d array integer
# replace with 1 as a wall and 0 as a space
for i in range(row):
    content[i] = content[i].replace("\n",'')
    for j in range(col):
        if content[i][j] == '#':
            solveMaze[i][j] = 1
        else:
           solveMaze[i][j] = 0
  
check = [[solveMaze[i][j] for j in range(col)] for i in range(row)]


changeX = [0,0,1,-1]
changeY = [1,-1,0,0]

# apply searching algorithms to solve the maze
def mazeSolver(start_pos):
    queue = []
    path_finder = {}
    queue.append(start_pos)
    node_visited = [start_pos]
    
    for i in range(row):
        for j in range(col):
            if solveMaze[i][j] == 0:
                path_finder[(i,j)] = (-1,-1)
    path_finder[start_pos] = (0,0)
    while len(queue) != 0:
        position = queue.pop(0)

        for i in range(len(changeX)):
            newPositionX = position[0] + changeX[i]
            newPositionY = position[1] + changeY[i]
            if isValid(newPositionX,newPositionY) and (newPositionX, newPositionY) not in node_visited:
                queue.append((newPositionX,newPositionY))
                solveMaze[newPositionX][newPositionY] = -1
                path_finder[(newPositionX,newPositionY)]=position
    return path_finder

# a function to check if it is possible to change X and Y position
def isValid(positionX, positionY):
    if  positionX < row and positionY < col and positionX>=0 and positionY>=0 and solveMaze[positionX][positionY] == 0 and solveMaze[positionX][positionY]!=-1 :
        return True
    return False


# A function to detect the only one entrance of a maze
# if the position of a maze equall 0, return that position as an entrance
def findEntrance():
    srt_pos = []
    for i in range(row):
        if solveMaze[i][0] == 0:
           srt_pos.append((i,0))
    return srt_pos

# detect the exist in the maze and print the path
# if we can not find a path, print Maze can not be solved
def printResult():
    result = []
    entrance = findEntrance()
    for start_pos in entrance:
        path = mazeSolver(start_pos)
        exists = (-1,-1)
        for coord in path.keys():
            if coord[1] == col-1:
                exists = (coord)
                break
        if path[exists]== (-1,-1):
            print("Maze can not be solved!")
            sys.exit() 
        helper = exists
        result.append(helper)
        while True:
            helper = path[helper]
            if helper == (0,0):
                return result
            else:
                result.append(helper)

pathResult = printResult()

# represent the solution path with *
for ele in pathResult:
   check[ele[0]][ele[1]] ='*'

# re-convert the maze
# * as a posible path and space as an imposible path
for i in range(row):
    for j in range(col):
        if check[i][j] == 1:
            check[i][j] = "#"
        elif check[i][j] == 0:
            check[i][j] = " "
    check[i]=''.join(check[i]) + '\n'

check = ''.join(check)
print(check)



    




