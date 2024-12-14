from dataclasses import dataclass
from enum import Enum, auto
'''
Написати систему, яка буде допомагати працювати машину для продуктів
'''

# name, price, calories
# class Product:
#     def __init__(self, name, price, calories):
#         self.name = name
#         self.price = price
#         self.calories = calories

class Ingredient(Enum):
    E123 = auto()
    E524 = auto()

@dataclass(eq=False, frozen=False)
class Product:
    '''
    Class to store product information
    '''
    name: str
    price: float
    calories: float
    ingredients: list[Ingredient]

@dataclass
class Drink(Product):
    '''
    Class to store drink information
    '''
    taste: str


@dataclass
class Snack(Product):
    weight: float

'''
Написати функцію, яка буде приймати список продуктів та рахувати загальну суму
'''
def calculate_product_sum(product_list: list[Product]) -> float:
    result_sum = 0
    for product in product_list:
        print(product.price)
        result_sum += product.price
    return result_sum

def names_of_product(product_list: list[Product]) -> str:
    result_str = ''
    for product in product_list:
        print(product.price)
        result_str += str(product.name) + ', '
    return result_str

# print(__name__)
if __name__ == '__main__':
    fanta = Drink("Fanta", 30, 100, [Ingredient.E123, Ingredient.E524], 'orange')

    for ingredient in Ingredient:
        print(ingredient.name)
        if (ingredient.name == 'E123'):
            print('Correct!')

# print(type(Ingredient.E123))
# cola = Drink("Cola", 50, 100, 'diet')

# product_list = [fanta, cola]
# print(names_of_product(product_list))


# print(product_list)
# product = Product("Snickers", 100, 1000)
# product_two = Product("Product", 100, 1000)

# print(product)
# print(product_two)
# print(product == product_two)

# product_two.name = 'Product Two'
# print(product_two)

# product_set = {Product("Snickers", 100, 1000), Product("Snickers", 100, 1000), Product("Snickers", 100, 1000), Product("Snickers", 100, 1000)}
# print(product_set)

# print({Product("Snickers", 100, 1000): "hello", Product("Snickers", 100, 1000): 'world'})

# Product -> Drink, Snack
