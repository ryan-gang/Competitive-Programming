# %%
fhand = open("g:\\Coding\\adventofcode\\expenseReport.txt") 
mytxt = fhand.read()
fhand.close()
# %%
num = mytxt.split("\n")
# %%
for i in range(len(num)):
    for j in range(len(num)):
        for k in range(len(num)):
            if (i == j):
                continue
            elif ((int(num[i]) + int(num[j]) + int(num[k])) == 2020):
                print(num[i], num[j], num[k])
                break