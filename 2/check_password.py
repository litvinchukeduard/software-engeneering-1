import re

def check_password(password: str) -> bool:
    pattern = r"(?=.*\d)(?=.*[A-Z])(?=.*[+=-\\])[\w\d+=-\\]{8}"
    []
    return bool(re.fullmatch(pattern, password))


assert check_password('password') == False
assert check_password('aaaaaA_4') == True
