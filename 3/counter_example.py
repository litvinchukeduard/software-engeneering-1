from collections import Counter
'''
У файлі записані випадкові числа 5, 0, 5, 3, 7, 3, 8, 7, 1, 4, 1, 0, 3, 5, 3, 5, 6, 0, 7, 9, 0, 8, 9, 4, 2, 3, 3, 2, 7, 1
Потрібно написати функцію, яка буде рахувати кількість появи кожного числа, які вона запише у файл, та виведе найчастіше число у термінал
'''

# {'5': 4, '0': 3}
def get_file_statistics(file_path: str):
    statistics_dict = dict()
    with open(file_path) as file:
        numbers = file.readline().split(', ')
        for number in numbers:
            if number in statistics_dict:
                statistics_dict[number] += 1
                continue
            statistics_dict[number] = 1
    print(statistics_dict)
            

# get_file_statistics('example_file.txt')

numbers = [5, 0, 5, 3, 7, 3, 8, 7, 1, 4, 1, 0, 3, 5, 3, 5, 6, 0, 7, 9, 0, 8, 9, 4, 2, 3, 3, 2, 7, 1]
# print(Counter(numbers))
counter = Counter(numbers)
print(counter.most_common(1))
