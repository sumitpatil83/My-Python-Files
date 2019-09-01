import os
from pathlib import Path
for f_name in os.listdir('./'):
    if f_name.endswith('.txt'):
        print(f_name)


p = Path('./')
try:
    p.mkdir(exist_ok=True)
except FileExistsError as exc:
    print(exc)

entries = os.listdir('./')
for entry in entries:
    print(entry)

with open('data.txt', 'r') as f:
    data = f.read()

with open('data.txt', 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)
