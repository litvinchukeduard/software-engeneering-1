from datetime import datetime
from collections import UserList
'''
Створити систему, яка буде працювати з повідомленнями

User(first_name, last_name, phone_number)
Message(message_text, author, recepient, creation_time)

MessageSystem(messages)

- додати метод, який буде виводити усі повідомлення від користувача до користувача
- додати метод, який виводить усіх людей, яким користувач колись писав
'''


class User:
    def __init__(self, first_name: str, last_name: str, phone_number: str):
        self.__first_name = None
        self.first_name = first_name
        self.last_name = last_name
        self.__phone_number = None
        self.phone_number = phone_number

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, new_name: str):
        if len(new_name) == 0:
            raise ValueError('First name is not valid')
        self.__first_name = new_name

    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, new_number: str):
        if len(new_number) == 0:
            raise ValueError('Phone number is not valid')
        self.__phone_number = new_number

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def __repr__(self):
        return str(self)

# user = User('Ihor', 'Last name', '1234567890')
# user.phone_number = ''

class Message:
    def __init__(self, message_text: str, author: User, recepient: User):
        self.message_text = message_text
        self.author = author
        self.recepient = recepient
        self.__creation_date = datetime.now()
        # self.creation_date = datetime.now()

    @property
    def creation_date(self):
        return self.__creation_date
    
    @creation_date.setter
    def creation_date(self, _):
        raise Exception("Can not assign a new value to creation date")
    
    def __str__(self):
        return f'From "{self.author}" to "{self.recepient}" {self.message_text} | {self.creation_date}'
    
    def __repr__(self):
        return str(self)
    
    def __lt__(self, other):
        if not isinstance(other, Message):
            raise TypeError(f'Can not compare Message to this type {type(other)}')
        return self.creation_date < other.creation_date
    

class MessageSystem(UserList):
    def __init__(self, messages: list[Message] = []):
        super().__init__(messages)
        # self.data = messages

    def find_all_messages(self, user_one: User, user_two: User):
        result_messages = []
        # Пройтися по усім повідомленням
        for message in self.data:
            # Всередині одного повідомлення дістати автора та отримувача
            # Зробити перевірку:
            if message.author == user_one and message.recepient == user_two:
                result_messages.append(message)
            if message.author == user_two and message.recepient == user_one:
                result_messages.append(message)
                # Чи автор це є user_one та отримувач це є user_two
                # Чи автор це є user_two та отримувач це є user_one
        return sorted(result_messages)
    
    def find_all_chats(self, user: User) -> list[User]:
        user_set = set()
        # Пройтися по усім повідомленням
        for message in self.data:
            # Зробити перевірку:
            # Всередині одного повідомлення дістати автора та отримувача
            # if message.author == user or message.recepient == user:
            
            # Якщо автор - юзер:
            if message.author == user:
                user_set.add(message.recepient)
                # додати отримувача

            # Якщо отримувач юзер:
            if message.recepient == user:
                user_set.add(message.author)
                # додати автора

            # Якщо юзер і автор і отримувач:
                # додати юзера
        return user_set
            




user_one = User("Ihor", "Last name", "1234567890")
user_two = User("Jane", "Last name", "0987654321")

user_three = User("Jane", "Last name", "0987654321")

message_one = Message("Hello", user_one, user_two)
message_two = Message("Hello, Ihor", user_two, user_one)
message_three = Message("How are you doing?", user_one, user_two)

message_four = Message("TODO: clean the dishes", user_one, user_one)

print(message_two)

# message_one < 1



messages_list = [message_three, message_two, message_one, message_four]
# print(message.message_text)
# print(message.creation_date)

# message.creation_date = datetime(2025, 1, 12)
# message._Message__creation_date = datetime(2025, 1, 12)
# print(dir(message)) 
# print(message.message_text)
# print(message.creation_date)

message_system = MessageSystem(messages_list)
print(message_system.find_all_chats(user_one))
# print(message_system.find_all_messages(user_one, user_two))

# my_set = {}
# print(type(my_set))
