from pathlib import Path
import shutil

base = Path.home() / "PycharmProjects" / "Advanced Topics in Python"
src = base / "files"
dst = base / "files_backup"

shutil.copytree(src, dst, dirs_exist_ok=True)
