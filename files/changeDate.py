import os, re, shutil
from pathlib import Path

original_folder = Path(r'C:\Users\haama\PycharmProjects\Advanced Topics in Python\files\newFolder')
temp_folder = Path(r'C:\Users\haama\PycharmProjects\Advanced Topics in Python\files\tempFolder')
final_folder = Path(r'C:\Users\haama\PycharmProjects\Advanced Topics in Python\files\renamedFolder')

if not original_folder.exists():
    print(f"Folder not found: {original_folder}")
    exit()

temp_folder.mkdir(exist_ok=True)

pattern = re.compile(
    r"^(?P<before>.*?)(?P<month>0[1-9]|1[0-2])-(?P<day>0[1-9]|[12][0-9]|3[01])-(?P<year>\d{4})(?P<after>.*)$"
)

for filename in os.listdir(original_folder):
    src_path = original_folder / filename
    if not src_path.is_file():
        continue

    match = pattern.search(filename)
    if match:
        before = match.group("before")
        day = match.group("day")
        month = match.group("month")
        year = match.group("year")
        after = match.group("after")
        new_name = f"{before}{day}-{month}-{year}{after}"
    else:
        new_name = filename

    dst_path = temp_folder / new_name

    if dst_path.exists():
        print(f"Skipped (exists): {new_name}")
        continue

    shutil.copy2(src_path, dst_path)
    print(f"Copied: {filename} -> {new_name}")

# copy to final
shutil.copytree(temp_folder, final_folder, dirs_exist_ok=True)
print(f"Copied all to final folder: {final_folder}")

# cleanup
if temp_folder.exists():
    shutil.rmtree(temp_folder)
    print("Temporary folder deleted.")
