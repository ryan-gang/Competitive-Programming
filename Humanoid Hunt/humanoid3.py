# %%
# Solution to Puzzle 3 of the Humanoid Hunt
# Created by Ritayan Ganguly
# 09/02/2021

input_data = open("input3.txt", "r+").read().strip()
print("Signal received. Characters read : ", end = "")
print(len(input_data))


# %%
connections_list = input_data.split("\n")
MaxLength = 0
for i in connections_list:
    X, Y = [int(j) for j in i.split(" ")[0].split(",")]
    # print(X,Y)
    try:
        Z = len(i.split(" ")[1])
        # print(Z)
        MaxLength = max(MaxLength, max(X, Y) + Z)
    except:
        # print(0)
        MaxLength = max(MaxLength, max(X,Y))
        
print(MaxLength)
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
    array[X][Y] = 1
    next_move = connection_string[index]
    direction = get_direction(next_move)
    X += direction[0]
    Y += direction[1]
    index += 1
# %%
print("Starting analysis.")
# first_char = get_first_char(input_data)
# password = get_rest_chars(input_data, first_char)
print("Analysis finished.\nPassword is : ", end="")
# print(password)
