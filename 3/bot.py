from decimal import Decimal, InvalidOperation
from colorama import Fore, Back, Style
'''
Написати бот, який буде приймати перелік чисел або (exit) і рахувати сумму
'''

'''
100.02
1.01
1.1
2
30
exit
'''

# 134
# Decimal(1.01)

# try:
#     1 / 0
# except ZeroDivisionError:
#     print('Divided by zero')

number_sum = Decimal(0)
while True:
    user_input = input(Fore.BLUE + "Enter next number: " + Fore.YELLOW)
    if user_input == 'exit':
        print(Fore.GREEN + "Goodbye!")
        break
    # new_number = Decimal(float(user_input)) # Не вірно!
    try:
        new_number = Decimal(user_input)
    except InvalidOperation:
        print(Fore.RED + "Try to enter number again...")
        continue
    number_sum += new_number
    print(Fore.GREEN + str(number_sum))
