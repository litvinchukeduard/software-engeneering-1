"""
Write a code that orders collection of Uris based on it's domain next way that it will returns at first Uris with domain "com", "gov", "org" (in alphabetical order of their domains), and then all other Uris, ordered in alphabetical order of their Top Level Domains (TLD, the part of Uri after last dot). In addition to that:

    content of Uri should not be changed,
    other part of Uri doesn't affect sorting. (uris "c.com","b.com","a.com" can be placed in any order inside their group, so both "c.com","b.com","a.com" and "a.com","c.com","b.com" are correct, till they are stand before *.org)

e.g.

"http://www.google.en/?x=jsdfkj"
"http://www.google.de/?x=jsdfkj"
"http://www.google.com/?x=jsdfkj"
"http://www.google.com/?x=jsdfkj"
"http://www.google.org/?x=jsdfkj"
"http://www.google.gov/?x=jsdfkj"

should be sorted into

"http://www.google.com/?x=jsdfkj"
"http://www.google.com/?x=jsdfkj"
"http://www.google.gov/?x=jsdfkj"
"http://www.google.org/?x=jsdfkj"
"http://www.google.abc/?x=jsdfkj"
"http://www.google.de/?x=jsdfkj"
"http://www.google.en/?x=jsdfkj"

In the final tests consecutive addresses with the same domain will be grouped and sorted before comparison, i.e.:

Given your solution returns ["b.com", "a.com", "c.gov"], the tests will do this:

    Split the addresses into groups: [["b.com", "a.com"], ["c.gov"]]
    Sort each group: [["a.com", "b.com"], ["c.gov"]]
    Flatten them: ["a.com", "b.com", "c.gov"]


"""

def string_length_key(s: str) -> int:
    return len(s)


# my_list_one = [5, 4, 3, 2, 1]
# my_list_two = ["b", "c", "a"]
# my_list_three = ['abc', 'a', 'cd'] # [3, 1, 2] -> [1, 2, 3] -> ['a', 'cd', 'abc']
# print(sorted(my_list_two, reverse=True))

# print(sorted(my_list_three, key=string_length_key))

urls = [
    "http://www.google.en/?x=jsdfkj",
    "http://www.google.de/?x=jsdfkj",
    "http://www.google.com/?x=jsdfkj",
    "http://www.google.com/?x=jsdfkj",
    "http://www.google.org/?x=jsdfkj",
    "http://www.google.gov/?x=jsdfkj",
]

def get_top_level_domain(url: str) -> str:
    url_part = url.split('//')[-1]
    main_url = url_part.split('/')[0]
    return main_url.split('.')[-1]

# print(get_top_level_domain(urls[1]))

my_tuple = (1, 2)
my_tuple_two = (1, 3)
# my_tuple[1] = 3

# print(my_tuple < my_tuple_two)

# if my_tuple[0] <= my_tuple_two[0] and my_tuple[1] < my_tuple_two[1]:
    # print('Pass')

"com", "org", "gov"
"abc", "en", "de"


tld = "com"
# if tld in ["com", "org", "gov"]:
#     print((0, tld))
# else:
#     print((1, tld))

print((0, tld) < (0, "en"))
