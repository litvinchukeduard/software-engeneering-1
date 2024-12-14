from dataclasses import dataclass

@dataclass
class Drink:
    taste: str

@dataclass
class Snack:
    weight: float


@dataclass
class IceCream(Snack, Drink):
    pass
