# from collections import defaultdict
# # Solution to Puzzle 2 of the Humanoid Hunt
# # Created by Signe Klinting
# # 2021-01-09

# %%
def make_empty_array(size):
    rows, cols = (size, size) 
    array = [[0 for i in range(cols)] for j in range(rows)] 
    return array

# %%

def get_direction(direction):
    if (direction == "D"):
        return(0, -1)
    elif (direction == "U"):
        return(0, 1)
    elif (direction == "R"):
        return(1, 0)
    elif (direction == "L"):
        return(-1, 0)
# %%

MaxLength = 2
connections_list = ['0,0 L,L,D,D,R,R']
data = connections_list[0]
startX, startY = data.split(" ")[0].split(",")
connection_string = data.split(" ")[1].split(",")

array = make_empty_array(MaxLength)
print(connection_string)
for i in connection_string:
    print(i)

def insert_array_element(startX, startY, connection_string):
    index = 0
    X = startX
    Y = startY
    while(True):
        array[X][Y] = 1
        next_move = connection_string[index]
        direction = get_direction(next_move)
        X += direction[0]
        Y += direction[1]
        index += 1

    # It's all fine and all but what happens when the X,Y go to the negative direction?
    # Either make the array of size 2*MaxLength+1 
    # ------MaxLength------0------MaxLength------
    # Meh Later

# %%
index = 0
X = int(startX)
Y = int(startY)
while(True):
    array[X][Y] = 1
    next_move = connection_string[index]
    direction = get_direction(next_move)
    X += direction[0]
    Y += direction[1]
    index += 1
