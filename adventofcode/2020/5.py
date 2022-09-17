# %%
# input_data = input()
# input_data = "FBFBBFFRLR"

def get_seatId(input_data):
    rows = input_data[:-3]
    cols = input_data[-3:]

    total_rows = 128
    total_cols = 8
    min_rows = 0
    min_cols = 0
    current_row = 0
    current_col = 0
    for direction in rows:
        if (direction == "F"):
            total_rows = (min_rows + total_rows)/2
        else :
            min_rows = (min_rows + total_rows)/2
            
    # print(min_rows, total_rows)
    # print(rows[-1])
    if (rows[-1] == "F"):
        final_row = total_rows - 1
        # print(final_row)
    else:
        final_row = min_rows
        # print(final_row)


    for direction in cols:
        if (direction == "L"):
            total_cols = (min_cols + total_cols)/2
        else:
            min_cols = (min_cols + total_cols)/2
            

    if (cols[-1] == "L"):
        final_col = (total_cols - 1)
        # print(final_col)
    else:
        final_col = min_cols
        # print(final_col)

    seat_Id = final_row * 8 + final_col
    # print("Seat ID : ", seat_Id)
    return seat_Id
# %%

fhand = open("g:\\Coding\\adventofcode\\2020\\5.txt") 
input_data = fhand.read()
fhand.close()
data = input_data.split("\n")
max_Id = 0
for i in data:
    Id = get_seatId(i)
    if (Id > max_Id):
        max_Id = Id

print("Maximum Seat Id :", max_Id)

# %%
all_ids = []
for Ids in range(1,int(max_Id)):
    all_ids.append(Ids)

# %%
for i in data:
    Id = get_seatId(i)
    if Id in all_ids:
        all_ids.remove(Id)
        
# %%
out = [ i for i in all_ids if i > 5 ]
print(out)
# %%
