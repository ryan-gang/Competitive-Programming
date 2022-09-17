# %%
# Use Regex to extract redit threads. 
# Its a website copied with all the other words intact
# Ritayan Ganguly
# 12/02/2021

# %%
import os
os.chdir(r"C:\Users\unitel\Desktop\Reddit")
os.listdir()

# %%
from os import listdir
from os.path import isfile, join
mypath = (r"C:\Users\unitel\Desktop\Reddit")
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

# %%
for files in onlyfiles:
    if (files.split(".")[1] == "txt"):
        print(files)
        
        
#######################################

# %%
os.chdir(mypath)
for files in onlyfiles:
    f = open(files,'r',encoding = 'utf-8')
    T = f.readlines()
    print(T[0])
    print("\n\n")
    f.close()
    
    
# %%
file_name = input("Enter file name")
f = open(file_name,'r',encoding = 'utf-8')
# All = f.readlines()
All = f.read()
print(All)
f.close()

# %%
Regex1 = "ago(.*?)Reply"
# Get all comments except the last one