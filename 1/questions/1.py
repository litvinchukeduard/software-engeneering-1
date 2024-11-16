"""
1) яка різниця між IS and ==
2) поясніть на прикладах **kwargs та  *args
3) поясніть на прикладах розпакування списків та словників
4) можемо пройтись ще по рекурсії (декілька прикладів)
"""

my_str_one = "hello"
my_str_two = "hello"

# print(my_str_one == my_str_two)
# print(my_str_one is my_str_two)

my_list_one = [1, 2, 3]
my_list_two = [1, 2, 3]

# print(my_list_one == my_list_two)
# print(my_list_one is my_list_two)

my_int_one = 1
my_int_two = 1

print(my_int_one == my_int_two) # По значенню
print(my_int_one is my_int_two) # По адресі у памʼяті
