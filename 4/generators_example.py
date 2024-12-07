import random
'''
Написати функцію-генератор, яка симулює кидання кубика
'''

def simulate_dice_throw(n: int):
    result = []
    for i in range(n):
        result.append(random.randint(1, 6))
    for number in result:
        yield number


def simulate_dice_throw_inplace(n: int):
    for i in range(n):
        yield random.randint(1, 6)


for random_number in simulate_dice_throw(3):
    print(random_number)


# generator = simulate_dice_throw(3)
# generator = (random.randint(1, 6) for i in range(3))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# print([random.randint(1, 6) for i in range(3)])

# generator = range(1, 4)
# print(next(generator))
# print(next(generator))
# print(next(generator))

# result_list = []
# for i in range(6):
#     result_list.append(i)
# print(result_list)

# print([i for i in range(6)])
# generator = (i for i in range(6))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
