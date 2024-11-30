from pathlib import Path
from colorama import Fore

p = Path('.')
# [x for x in p.iterdir() if x.is_dir()]

# for x in p.iterdir():
#     if x.is_dir():
#         print(Fore.YELLOW + 'Folder: ' + str(x))
#     else:
#         print(Fore.GREEN + 'File: ' + str(x))

result_list = []
for x in p.iterdir():
    if x.is_dir():
        result_list.append(x)

print(result_list)

