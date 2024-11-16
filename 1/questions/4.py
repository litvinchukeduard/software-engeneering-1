"""
1) яка різниця між IS and ==
2) поясніть на прикладах **kwargs та  *args
3) поясніть на прикладах розпакування списків та словників
4) можемо пройтись ще по рекурсії (декілька прикладів)
"""

def factorial(n: int) -> int:
    """Function to calculate a factorial"""
    product = 1
    # for (i = 0; i < n; i+= 1)
    # 5! = 1 * 2 * 3 * 4
    for i in range(1, n + 1):
        product *= i
    return product

# 5! = 5 * factorial(n - 1) 
# n! = n * factorial(n - 1)
# ...
# 5! = 5 * 4 * 3 * 2 * 1

# 5! = 5 * factorial(4)
# 4! = 4 * factorial(3)
# ...
# 2! = 2 * factorial(1)
# 1! = 1

# 2! = 2 * 1 = 2
# 3! = 3 * factorial(2) = 6
# ...

def factorial_recursive(n: int, level: int = 0) -> int:
    """Recursive function to calculate a factorial"""
    # Випадок, коли рекурсія зупиняється
    if n == 1:
        print(f"{level}: factorial(1) = 1")
        return 1

    # Рекурсивний крок
    print(f"{level}: factorial({n}) = {n} * factorial({n - 1})")
    result = n * factorial_recursive(n - 1, level=level + 1)
    print(f"{level}: factorial({n}) = {result}")

    # Повернення значення
    return result
    # return n * factorial_recursive(n - 1)


print(factorial_recursive(5))
