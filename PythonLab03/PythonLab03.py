import os
from pathlib import Path

for file in os.scandir(Path.cwd()):
    print(f"File: {file.name}")
    if (not file.name.__contains__(".py") or file.name.__contains__("PythonLab02")):
        continue
    print(f"Executing: {file.name}")
    exec(open(file).read())
    input()