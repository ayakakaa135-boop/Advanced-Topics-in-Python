from pathlib import Path
import shutil


import os
# الملف والمجلد اللي بدك تحذفيهم
file_path = Path(r"C:\Users\haama\PycharmProjects\Advanced Topics in Python\files\data1.txt")
folder_path = Path(r"C:\Users\haama\PycharmProjects\Advanced Topics in Python\files_backup")

# حذف الملف
file_path.unlink(missing_ok=True)  # مش رح يعطي خطأ إذا الملف مش موجود

# حذف المجلد مع كل محتواه
shutil.rmtree(folder_path, ignore_errors=True)  # يتجاهل الأخطاء لو المجلد مش موجود

