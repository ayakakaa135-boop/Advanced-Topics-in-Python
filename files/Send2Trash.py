from pathlib import Path
from send2trash import send2trash

# الملفات والمجلدات اللي بدك تحذفيهم
paths = [
    Path(r"C:\Users\haama\PycharmProjects\Advanced Topics in Python\files\data1.txt"),
    Path(r"C:\Users\haama\PycharmProjects\Advanced Topics in Python\files_backup")
]

for p in paths:
    if p.exists():
        send2trash(p)

print("Files/folders sent to trash!")
