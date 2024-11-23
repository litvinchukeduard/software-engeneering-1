import re
'''
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.
Examples (Input --> Output)

"1234"   -->  true
"12345"  -->  false
"a234"   -->  false


'''

def validate_pin(pin):
    # return true or false
    # len(pin)...
    pattern = r'\d{4}|\d{6}'
    # return re.fullmatch(pattern, pin) is not None
    return bool(re.fullmatch(pattern, pin))

# print(validate_pin("123456"))

assert validate_pin("1234") == True
assert validate_pin("1234sgddg") == False
assert validate_pin("123456") == True
assert validate_pin("12345") == False
assert validate_pin("a234") == False
