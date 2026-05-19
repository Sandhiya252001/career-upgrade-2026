import os
print(os.getcwd())
print(os.listdir())
# os.makedirs("sample")

from pathlib import Path
for file in Path(".").iterdir():
    print(file)