import zipfile
from pathlib import Path

folder_path = Path(r"C:\Users\haama\PycharmProjects\Advanced Topics in Python\files")
zip_path = folder_path.parent / "files_archive.zip"  # ملف ZIP بجانب المجلد

with zipfile.ZipFile(zip_path, 'w') as zipf:
    for file in folder_path.iterdir():
        if file.is_file():
            zipf.write(file, arcname=file.name)  # بدون المسار الكامل داخل ZIP

print("All files zipped!")
