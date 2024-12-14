from product import Product, Drink, Ingredient


class ProductTypeError(TypeError):
    pass


class IncorrectAmountOfMoneyError(Exception):
    pass


class VendingMachine:
    def __init__(self, product_list: list[Product] = []):
        self.products_list = product_list

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise ProductTypeError('This method only accepts Product and sub-types')
        self.products_list.append(product)
    
    def buy_product(self, amount_of_money: float):
        for product in self.products_list:
            if product.price == amount_of_money:
                return product
        raise IncorrectAmountOfMoneyError('Please enter a correct amount of money')

try: 
    fanta = Drink("Fanta", 30, 100, [Ingredient.E123, Ingredient.E524], 'orange')
    vending_machine = VendingMachine()
    # vending_machine.add_product(100)
    vending_machine.add_product(fanta)
    print(vending_machine.buy_product(10))
except TypeError:
    print('Please provide a Product type to method add_product')
except IncorrectAmountOfMoneyError:
    print('Please provide a Product type to method add_product')
except Exception:
    print('Exception happened')

# vending_machine.add_product("Cola")
# # vending_machine.add_product()

# print(vending_machine.products_list)

# print(isinstance(True, int))
# print(type(True) == bool)

# class bool(int)

# if (1, 0)
# if ([]):
#     print('True')

