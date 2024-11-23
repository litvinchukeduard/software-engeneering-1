from datetime import datetime

'''
Написати функцію, яка буде рахувати вік людини
'''

def calculate_age(date_string: str) -> int:
    # datetime.strptime # str parse time
    # datetime.strftime # str format time
    birthday_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    today = datetime.today().date()
    # today = datetime(year=2001, month=2, day=28).date()
    # return (today - birthday_date).days // 365
    years_difference =  today.year - birthday_date.year

    if today < birthday_date.replace(year=today.year):
        years_difference -= 1

    return years_difference
    # return today.year - birthday_date.year

# 23.11
# 24.11


# yyyy-mm-dd
print(calculate_age("2000-01-01")) # 24
print(calculate_age("2000-11-24"))
