fhand = open("g:\\Coding\\adventofcode\\2.txt") 
input = fhand.read()
fhand.close()
print(input)
# %%
data = input.split("\n")
for i in data:
    print(i)
    break
# %%
def get_valid_passwords(password):
    count = 0

    for character in password:
        if (character == letter):
            count += 1

    if count in range(lower_limit, upper_limit+1):
        print(password)   
        return True
    return False
# %%
valid_passwords = 0
for i in data:
    rules = i.split(":")[0]
    limits = rules.split(" ")[0]
    lower_limit = int(limits.split("-")[0])
    upper_limit = int(limits.split("-")[1])
    letter = rules.split(" ")[1]
    password = i.split(":")[1]
    if (get_valid_passwords(password)):
        valid_passwords += 1
        
print(valid_passwords)
