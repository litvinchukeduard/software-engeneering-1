import random
from string import ascii_uppercase, digits, punctuation, ascii_letters
'''
Написати функцію, яка буде генерувати випадковий пароль

1) Має бути принаймні одне число
2) Приймні одна літера у верхньому регістрі
3) Принаймні один спеціальний символ
4) Мінімальна довжина має бути 8
'''

# "1Mdfgdfdg" -> shuffle

symbols = ascii_uppercase + digits + punctuation + ascii_letters

def generate_random_password(length=8) -> str:
    # random.randint(0, 9)
    # random.choice("0123456789")
    if length < 8:
        raise ValueError('Password must be at least 8 symbols long')
    
    digit = random.choice(digits)
    uppercase_letter = random.choice(ascii_uppercase)
    special_character = random.choice(punctuation)

    new_password = [digit, uppercase_letter, special_character]
    for _ in range(length - 3):
        new_password += random.choice(symbols)

    random.shuffle(new_password)

    return ''.join(new_password)


# print(generate_random_password(1))
print(generate_random_password(20))

# ['h', 'e', 'l'][1] = '1'

# print("".join(['hello', 'world', 'people']))
