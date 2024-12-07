'''
Протягом року друзі збирали гроші, порахувати середні значення загалом та для кожного, дізнатись хто назбирав найбільше
'''

friend_savings = {
    "Alice": [100.50, 150.25, 200.75, 180.30, 210.40, 190.60, 220.80, 240.90, 260.10, 280.20, 300.50, 320.75],
    "Bob": [80.25, 120.75, 160.50, 140.20, 170.90, 150.60, 180.40, 200.30, 220.10, 240.25, 260.50, 280.75],
    "Charlie": [70.75, 110.30, 150.60, 130.90, 160.20, 140.40, 170.80, 190.90, 210.10, 230.25, 250.50, 270.75]
}

def compare_friend_tuples(t: tuple[str, float]) -> float:
    return t[1]

def find_max_savings(friend_savings: dict[str, list[float]]) -> tuple[str, float]: # ('Bob', 1000) 
    tuple_list = []
    for (name, savings_list) in friend_savings.items():
    # print(friend_savings.items())
        # print(name)
        # print(savings_list)
        tuple_list.append((name, sum(savings_list)))
    # print(tuple_list)
    # return max(tuple_list, key=compare_friend_tuples)
    return max(tuple_list, key=lambda t: t[1])
        
print(max(
    [
        (name, sum(savings_list))
        for (name, savings_list) in friend_savings.items()
    ]
    , key=lambda t: t[1]))

# print(find_max_savings(friend_savings))
