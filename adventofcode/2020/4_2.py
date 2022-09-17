# %%
fhand = open("g:\\Coding\\adventofcode\\2020\\4.txt") 
input_data = fhand.read()
fhand.close()
data = input_data.split("\n\n")   
# %% 
count = 0

for sample in data:
    all_lines = sample.split("\n")
    dictionary = get_dict(all_lines)
    if (valid_password_from_dict(dictionary)):
        count += 1
    else:
        pass

print(count)
# %%
def get_dict(all_lines):
    dict = {}
    for line in all_lines:
        parts = line.split(' ')
        for part in parts:
            keyword = part.split(':')[0]
            value = part.split(':')[1]
            dict[keyword] = value
    
    return dict

# %%
def valid_password_from_dict(dictionary):
    REQUIRED_KEYWORDS = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    #To delete a key regardless of whether it is in the dictionary, use the two-argument form of pop()
    dictionary.pop("cid", None)
    if (all(name in dictionary.keys() for name in REQUIRED_KEYWORDS)):
        if (automatic_validation(dictionary)):
            return True
    else:
        return False

# %%
# Returns 7 if valid dictionary else false
def automatic_validation(dictionary):
    import re
    count = 0
    byr = int(dictionary["byr"])
    if (byr >= 1920 and byr <= 2020):
        count += 1
        
    iyr = int(dictionary["iyr"])
    if (iyr >= 2010 and iyr <= 2020):
        count += 1
    
    eyr = int(dictionary["eyr"])
    if (eyr >= 2020 and eyr <= 2030):
        count += 1
    
    hgt = dictionary["hgt"]
    unit = hgt[-2:]
    try:
        value = int(hgt[:-2])
    except ValueError:
        value = 0
    if (unit == "cm" and (value in range(150,194))):
        count += 1
    elif (unit == "in" and (value in range(59,77))):
        count += 1
        
    hcl = dictionary["hcl"]
    if (bool(re.match("^#[0-9a-f]{6}$", hcl))):
        count += 1
        
    ECL = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    ecl = dictionary["ecl"]
    if (ecl in ECL):
        count += 1
        
    pid = dictionary["pid"]
    if (bool(re.match("^[0-9]{9}$", pid))):
        count += 1
        
    
    if (count == 7):
        return True
    else:
        return False

# %%

# TESTING
sample = input()
all_lines = sample.split("\n")
dictionary = get_dict(all_lines)
if (valid_password_from_dict(dictionary)):
    print("YES")
else:
    print("NO")
