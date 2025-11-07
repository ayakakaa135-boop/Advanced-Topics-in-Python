from pathlib import Path

import os
print(os.getcwd())
#os.chdir(r'C:\Users\haama\Desktop\photo')
print(Path.home())

myfile = open (Path.home() / Path("Desktop" ,"photo","file.txt"),"r")

print(str(Path.home() / Path("Desktop" ,"photo","file.txt")))
print(myfile)
print(myfile.mode)
print(myfile.name)
print(myfile.read())
print(myfile.readline(4))
print(myfile.readlines())

lines = myfile.readlines()
print(lines[0:2])
i = 0
for line in lines:
    print(line)
    i+=1

    if i ==5:
        break


myfile.close()