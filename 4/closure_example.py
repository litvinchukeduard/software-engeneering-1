'''
Написати функцію, яка буде генерувати унікальний id
'''

# 10 John Smith
# 11 John Smith

# 1 2 3 4
unique_number = 1

def my_generate_unique_number():
    global unique_number
    next_unique_number = unique_number
    unique_number -= 1
    return next_unique_number

def generate_unique_numbers():
    global unique_number
    next_unique_number = unique_number
    unique_number += 1
    return next_unique_number

def unique_numbers_generator():

    unique_number = 1

    def generate_next_number():
        nonlocal unique_number
        next_unique_number = unique_number
        unique_number += 1
        return next_unique_number

    return generate_next_number


# print('Old', generate_unique_numbers())
# print('New', my_generate_unique_number())
# print('Old',generate_unique_numbers())
# print('Old',generate_unique_numbers())

# print(unique_numbers_generator.unique_number)

unique_numbers = unique_numbers_generator()
print(unique_numbers())
print(unique_numbers())
print(unique_numbers())
# print(unique_numbers())
# print(unique_numbers())

unique_numbers_two = unique_numbers_generator()
print(unique_numbers_two())

print(unique_numbers())
