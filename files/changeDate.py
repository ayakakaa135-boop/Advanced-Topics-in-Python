import os, re, shutil
from pathlib import Path

original_folder = Path(r'C:\Users\haama\PycharmProjects\Advanced Topics in Python\files\newFolder')
temp_folder = Path(r'C:\Users\haama\PycharmProjects\Advanced Topics in Python\files\tempFolder')
final_folder = Path(r'C:\Users\haama\PycharmProjects\Advanced Topics in Python\files\renamedFolder')


temp_folder.mkdir(exist_ok=True)

pattern = r"^(?P<before>.*?)(?P<month>0[1-9]|1[0-2])-(?P<day>0[1-9]|[12][0-9]|3[01])-(?P<year>\d{4})(?P<after>.*)$"

for filename in os.listdir(original_folder):
    search = re.search(pattern, filename)
    src_path = original_folder / filename

    if search:
        before = search.group("before")
        day = search.group("day")
        month = search.group("month")
        year = search.group("year")
        after = search.group("after")
        new_name = f"{before}{day}-{month}-{year}{after}"
    else:
        new_name = filename

    dst_path = temp_folder / new_name
    shutil.copy(src_path, dst_path)


shutil.copytree(temp_folder, final_folder, dirs_exist_ok=True)


shutil.rmtree(temp_folder)