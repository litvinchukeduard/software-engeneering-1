import re

def check_password(password: str) -> bool:
    pattern = r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[+=-\\])[\w\d]{6}"
    return bool(re.fullmatch(pattern, password))

# regex=r"(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[\wA-Za-z]{6,}"

assert check_password('password') == False
assert check_password('aaaaaA_4') == True
