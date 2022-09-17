# %%
# import requests
# url = "https://adventofcode.com/2020/day/3/input"
# f = requests.get(url)
# print(f.text)
# %%
fhand = open("g:\\Coding\\adventofcode\\2020\\3.txt") 
input = fhand.read()
fhand.close()
data = input.split("\n")
for i in data:
    print(i)
    break
# %%
count = 0
trees = "#"
encounter = 0
for line in data:
    position = ((count*3 + 1)%len(line)) - 1 
    count += 1
    if (line[position] == trees):
        encounter += 1
print(encounter)
# %%
