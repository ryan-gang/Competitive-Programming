# %%
fhand = open("g:\\Coding\\adventofcode\\2020\\6.txt") 
input_data = fhand.read()
fhand.close()
# %%
group_data = input_data.split("\n\n")
count = 0
for data in group_data:
    individual_data = data.split("\n")
    length = (get_count_of_yes_answers(individual_data))
    count += length
    
print(count)
# %%
# Individual_data is an array of inputs of a group
def get_count_of_yes_answers(individual_data):
    yes_answers = []
    for data in individual_data:
        for question in data:
            if question not in yes_answers:
                yes_answers.append(question)
                
    return len(yes_answers)