# %%
fhand = open("g:\\Coding\\adventofcode\\2020\\9.txt") 
input_data = fhand.read()
fhand.close()
# %%
actual_data = input_data.split("\n")

# Check for negative numbers
count = 0
# for i in actual_data:
#     if (int(i) < 0):
#         count += 1
# print(count)

# %%

start_index = 25
final_index = len(actual_data)


# %%
    
for curr_index in range(start_index, final_index):
    eligible_list = []
    curr_num = int(actual_data[curr_index])
    curr_list = actual_data[curr_index-25:curr_index]
    for num in curr_list:
        if (int(num) < int(curr_num)):
            eligible_list.append(int(num))

    eligible_list.sort()

    flag = False
    for i in eligible_list:
        if (curr_num - i) in eligible_list:
            flag = True
        else:
            pass
    
    if (flag == False):
        print(curr_num)
# %%
arepl_filter = ["actual_data", "curr_list", "input_data", "fhand"]