import random

def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        print("Некоректні дані. Спробуйте ще раз. Введіть від 1 до 1000")
        return []

    lottery_numbers = []
    for i in range(quantity):
        lottery_numbers.append(random.randint(min, max))

    lottery_numbers.sort()
    return lottery_numbers
    

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)