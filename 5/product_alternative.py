from enum import Enum, StrEnum, auto

product_types = {"DRINK": "drink", "SNACK": "snack"}

class ProductTypes(StrEnum):
    DRINK = auto()
    SNACK = auto()

class Product:
    def __init__(self, name, price, calories, product_type: ProductTypes):
        self.name = name
        self.price = price
        self.calories = calories
        self.product_type = product_type


print(ProductTypes.DRINK.value)
print(ProductTypes.SNACK.value)

product = Product("Product", 100, 100, ProductTypes.DRINK)
print(product.product_type.value)

# if (value == ProductTypes.DRINK)
