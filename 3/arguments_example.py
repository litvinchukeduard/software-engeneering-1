'''
Написати додаток, який буде читати що є всередині файлу

python3 arguments_example.py main.py


'''

import sys
# folder_path = input("Enter folder path: ")
# print(sys.modules)
print(sys.argv)
if len(sys.argv) < 2:
    print('Usage:')
    print('\tpython3 arguments_example.py pictures')
    print('\tpython3 arguments_example.py <folder_path>')
    sys.exit()
file_path = sys.argv[1]

# file = open(file_path)
# print(file.read())
# file.close()

with open(file_path) as file:
    print(file.read())
# print("Hello")