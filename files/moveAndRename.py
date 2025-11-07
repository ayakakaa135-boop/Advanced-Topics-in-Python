import shutil
from pathlib import Path

project = Path(r"C:\Users\haama\PycharmProjects\Advanced Topics in Python")
src = project / "files" / "data.txt"
dst_folder = project / "files_backup"
dst_folder.mkdir(exist_ok=True)

dst = dst_folder / src.name
i = 1
while dst.exists():
    dst = dst_folder / f"data_{i}.txt"
    i += 1

shutil.move(src, dst)
print(f"File moved as {dst.name}")
