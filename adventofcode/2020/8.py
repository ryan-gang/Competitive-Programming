# %%
fhand = open("g:\\Coding\\adventofcode\\2020\\8.txt") 
input_data = fhand.read()
fhand.close()
# %%
actual_data = input_data.split("\n")
# %%
def func8_1(actual_data):
    visited = []
    accumulator = 0
    index = 0
    while(1):
        line = actual_data[index]
        instruction = line.split(" ")
        func = instruction[0]
        value = int(instruction[1])
        
        if (index not in visited):
            visited.append(index)
        else:
            break

        # print(index, end=", ")
        # print(accumulator, end = ", ")

        
        if (func == "nop"):
            pass
        elif (func == "acc"):
            accumulator += value
        elif (func == "jmp"):
            index += (value)
            continue


        index += 1
        
    return(accumulator)

print(func8_1(actual_data))    
# %%
visited = []
accumulator = 0
index = 0
while(1):
    line = actual_data[index]
    instruction = line.split(" ")
    func = instruction[0]
    value = int(instruction[1])
    
    if (index not in visited):
        visited.append(index)
    else:
        break

    print(index, end=", ")
    # print(accumulator, end = ", ")

    
    if (func == "nop"):
        pass
    elif (func == "acc"):
        accumulator += value
    elif (func == "jmp"):
        index += (value)
        continue


    index += 1
    
print(accumulator)
# %%
count = 0
for i in actual_data:
        line = i
        instruction = line.split(" ")
        func = instruction[0]
        value = int(instruction[1])
        if (func == "jmp" and value < 0):
            count += 1
            
print("\n")
print(actual_data[124])


# https://github.com/dedolence/AoC-2020-day08/blob/master/part2.py