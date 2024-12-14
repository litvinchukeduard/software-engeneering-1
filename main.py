from collections import UserDict
# # from module.function import hello
# from module_two.functions import world

# world()

class MyDict(UserDict):
    def do_something(self):
        self.get('key1')

my_regular_dict = {'key1': 1, 'key2': 2}
my_class_dict = MyDict({'key1': 1, 'key2': 2})
print(my_class_dict)

print(my_regular_dict['key1'])
print(my_class_dict['key1'])

my_class_dict.