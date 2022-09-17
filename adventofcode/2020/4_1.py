# %%
fhand = open("g:\\Coding\\adventofcode\\2020\\4.txt") 
input = fhand.read()
fhand.close()
data = input.split("\n\n")
# %%
for sample in data:
    print(sample)
    break
# %%
all_lines = sample.split("\n")
for line in all_lines:
    print(line)
    
# %%
def Valid_Password(lines):
    REQUIRED_KEYWORDS = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    keywords = []
    for line in lines:
        parts = line.split(' ')
        for part in parts:
            keyword = part.split(':')[0]
            keywords.append(keyword)
        
    if "cid" in keywords:
        keywords.remove("cid")

    keywords.sort() 
    if (keywords == REQUIRED_KEYWORDS):
        return True
    else:
        return False


# %%
count = 0

for sample in data:
    lines = sample.split("\n")
    if(Valid_Password(lines)):
        count += 1
        
print(count)
# %%