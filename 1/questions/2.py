"""
1) яка різниця між IS and ==
2) поясніть на прикладах **kwargs та  *args
3) поясніть на прикладах розпакування списків та словників
4) можемо пройтись ще по рекурсії (декілька прикладів)
"""

def print_values(*values, sep=" "):
    for value in values:
        print(str(value) + sep)
    # pass


# print_values("Hello", "World", 1, 2, 3, 4, 5, sep="_hello_")
# print_values()
# print("Hello", "World", 1, 2, 3, 4, 5)

def create_a_dict(**dict_values):
    print(dict_values)
    return dict_values

# create_a_dict(sep='1234', length=1234)

# print("Hello", "world", sep="|_hello__|")
my_list = [1, 2, 3, 4]
# print(my_list[0], my_list[1], my_list[2], my_list[3])
# print(*my_list)
# print_values(*my_list, sep="____")

my_dict = {'sep': '____'}
# print(1, 2, 3, **my_dict)

create_a_dict(**my_dict)
