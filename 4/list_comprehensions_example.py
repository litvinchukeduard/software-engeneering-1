'''
Написати функцію, яка буде приймати список зі слів та скорочувати їх
'''

#Hippopotomonstrosesquippedaliophobia
# 5
#Hip...

words_list = [
    "Hippopotomonstrosesquippedaliophobia",
    "Antidisestablishmentarianism",
    "Pneumonoultramicroscopicsilicovolcanoconiosis"
]

# def shorten_string(string_list: list[str], length: int) -> list[str]:
#     short_string_list = []
#     for string in string_list:
#         # print(string[:3])
#         short_string_list.append(f'{string[:length - 3]}...')
#     return short_string_list


# def shorten_string(string_list: list[str], length: int) -> list[str]:
#     '''
#     Function to shorten strings to certain length and adds '...'
    
#     If length is less than or equals to 3 then it raises an exception
#     '''
#     if length <= 3:
#         raise ValueError('Length can not be less than 3')
#     return [f'{string[:length - 3]}...' for string in string_list]

def shorten_string(string_list: list[str], length: int) -> list[str]:
    '''
    Function to shorten strings to certain length and adds '...'
    
    If length is less than or equals to 3 then it raises an exception
    '''
    if length <= 3:
        return ['...' for _ in string_list]
    return [f'{string[:length - 3]}...' for string in string_list]


print(shorten_string(words_list, 1))

# print("abcdef"[:-1])
