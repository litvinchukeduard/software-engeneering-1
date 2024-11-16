
'''
Написати функцію, яка буде рахувавати факторіал 
'''

# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 1! = 1
# 3! = 3 * 2 * 1 = 6

# /*
#  * Computes factorial
#  */
def factorial(n: int) -> int:
    """Function to calculate a factorial"""
    product = 1
    # for (i = 0; i < n; i+= 1)
    # 5! = 1 * 2 * 3 * 4
    for i in range(1, n + 1):
        product *= i
    return product


# factorial(2)
# factorial("Hello")
# print("Checking factorial for n = 5", factorial(5) == 120)
def test_factorial():
    assert factorial(5) == 120
    assert factorial(1) == 1
    assert factorial(3) == 6

# print(factorial(5))
test_factorial()
