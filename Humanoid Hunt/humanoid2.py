# %%
# Solution to Puzzle 2 of the Humanoid Hunt
# Created by Ritayan Ganguly
# 05/02/2021

input_data = open("input.txt", "r+").readline().strip()
print("Signal received. Characters read : ", end = "")
print(len(input_data))

# %%
def get_first_char(input_data):
    input_data_dict = {}
    for i in input_data:
        input_data_dict[i] = input_data_dict.get(i, 0) + 1
            
    for k in sorted(input_data_dict, key=input_data_dict.get, reverse=True):
        return k
    
# %%

def get_rest_chars(input_data, first_char):
    count = 1
    password = first_char
    output = ""

    while(True):
        dictionary = {}

        for index in range(len(input_data)):
            loop_data = (input_data[index:index+2])
            if loop_data[:-1] == password:
                key = loop_data[-1]
                dictionary[key] = dictionary.get(key, 0) + 1
                sorted_dictionary = sorted(dictionary, key = dictionary.get, reverse=True)
                
        for i in sorted_dictionary:
            new_password_character = i
            # print(new_password_character)
            break

        count += 1
        password = new_password_character
        output += new_password_character
                
        if ";" in output:
            return (first_char + output[:-1])


# %%
print("Starting analysis.")
first_char = get_first_char(input_data)
password = get_rest_chars(input_data, first_char)
print("Analysis finished.\nPassword is : ", end="")
print(password)
