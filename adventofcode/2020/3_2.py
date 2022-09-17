# %%
fhand = open("g:\\Coding\\adventofcode\\2020\\3.txt") 
input = fhand.read()
fhand.close()
data = input.split("\n")
for i in data:
    print(i)
    break
# %%
def trees_encountered(right_slope):
    count = 0
    trees = "#"
    encounter = 0
    for line in data:
        position = ((count*right_slope + 1)%len(line)) - 1 
        count += 1
        if (line[position] == trees):
            encounter += 1
    return(encounter)
# %%
print(trees_encountered(3))
print(trees_encountered(1))
print(trees_encountered(5))
print(trees_encountered(7))
# %% For the right 1, down 2.
count = 0
trees = "#"
encounter = 0
right_slope = 1
for i in range(len(data)):
    if (i % 2 != 0):
        continue
    else:
        line = data[i]
        position = ((count*right_slope + 1)%len(line)) - 1 
        count += 1
        if (line[position] == trees):
            encounter += 1
print(encounter)
# %%
trees_encountered(3) * trees_encountered(1) * trees_encountered(5) * trees_encountered(7) * 46
