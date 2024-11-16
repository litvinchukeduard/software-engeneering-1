'''
When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"
         "HEllOWOrld!"
         " " -> ""

Note: Y is not a vowel in this kata.
'''

def swap(text_string: str) -> str:
    vowels = "aeiou"
    # vowels = ["a", "e", "i", "o", "u"]
    #your code here
    result_string = ""
    for symbol in text_string:
        # print(symbol)
        # if symbol in vowels:
        #     result_string += symbol.upper()
        # else:
        #     result_string += symbol

        # symbol in vowels ? symbol.upper() : symbol
        result_string += symbol.upper() if (symbol in vowels) else symbol
    return result_string

# print("Hello" in [1, 2, 3])
assert swap("HelloWorld!") == "HEllOWOrld!"
assert swap("Monday") == "MOndAy"

# my_str = "Hello"
# my_str[1] = "E"
# print(my_str)