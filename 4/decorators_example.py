from datetime import datetime
from functools import wraps
'''
Написати декоратор-логувальник, який буде на виклик функції виводити назву функції, виводити аргументи та виводити час виконання
'''


'''
2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
'''

# def log_decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#         result = func(*args, **kwargs)
#         print(f'{timestamp} INFO Calling function: {func.__name__} with arguments {args} {kwargs}. With result: {result}')
#         return result
#     return wrapper

def log_decorator(level):
    def internal_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            result = func(*args, **kwargs)
            print(f'{timestamp} {level} Calling function: {func.__name__} with arguments {args} {kwargs}. With result: {result}')
            return result
        return wrapper
    return internal_decorator

@log_decorator('DEBUG')
def sum_numbers(a: int, b: int) -> int:
    '''A function to sum numbers from a to b'''

    result_sum = 0
    # print('DEBUG: create a variable to store sum, 0')
    for number in range(a, b + 1):
        result_sum += number
        # print('DEBUG: added number to sum, 0')
    # print('INFO returning result')
    return result_sum

@log_decorator('ERROR')
def return_hello():
    return 'Hello'

# 1 2 3
sum_numbers(1, 3)
sum_numbers(1, 3)
sum_numbers(1, 6)
sum_numbers(1, 9)
sum_numbers(2, 5)

return_hello()


# print(dir(sum_numbers))
# print(sum_numbers.__doc__)

