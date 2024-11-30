from colorama import Fore, Back, Style

# print(Fore.BLUE + Back.GREEN + Style.BRIGHT + 'some red text')
# print(Fore.GREEN + "Hello")

from colorama import init

init(autoreset=True)
print(Fore.RED + 'some red text')
print('automatically back to default color again')
