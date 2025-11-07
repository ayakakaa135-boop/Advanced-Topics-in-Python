from pathlib import Path

file_path = Path("data1.txt")

with open(file_path, 'w') as f:
    f.write("Hello Aya!\nWelcome to Python file handling.")

mylist = ['\n1', '\n2', '\n3']

with open(file_path, 'a') as f:
    f.writelines(mylist)

with open(file_path, 'r') as f:
    print(f.read())
