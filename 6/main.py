from datetime import datetime
from collections import UserList
import json

'''
Створити систему, яка буде працювати з повідомленнями

User(first_name, last_name, phone_number)
Message(message_text, author, recepient, creation_time)

MessageSystem(messages)

- додати метод, який буде виводити усі повідомлення від користувача до користувача
- додати метод, який виводить усіх людей, яким користувач колись писав
'''


'''

Потенційні проблеми:

1) Коли читати користувача, то на кожне повідомлення буде окремий користувач

{
    "messages": [
        {"author": {
                    "first_name": "Ihor"
                    }, ...
        },
        {"author": {
                    "first_name": "Ihor"
                    }, ...
        }
    ]
}

1.1) Якщо генерувати унікальний id, то після перезапуску коду, id буде починати з 0
'''

MESSAGES_FILE = "messages.json"


class User:
    id = 0

    def __init__(self, first_name: str, last_name: str, phone_number: str):
        User.id += 1
        self.id = User.id
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

    def to_json(self) -> str:
        return {
            "first_name": self.first_name, 
            "last_name": self.last_name, 
            "phone_number": self.phone_number, 
            "id": self.id
        }

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
    
    def to_json(self) -> str:
        result_dict = {
            "message_text": self.message_text,
            "creation_date": str(self.creation_date),
            "author": self.author.to_json(),
            "recepient": self.recepient.to_json()
        }

        return result_dict
    
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

    def save_to_file(self):
        with open(MESSAGES_FILE, 'w') as json_file:
            json.dump(self.data, json_file, default=lambda o: o.to_json(), indent=4)

    # def load_json_file(self):
    #     id_list = []
    #     user_list = []
    #     # Відкрити json файл та прочитати що є всередині list[dict]
    #     with open(MESSAGES_FILE, 'r') as json_file:
    #         json_list = json.load(json_file)
    #         # Пройтися по кожному повідомленю у списку
    #         for message in json_list:
    #             # Дістати автора, дістати отримувача
    #             author = message['author']
    #             recepient = message['recepient']
    #             # Перевірити чи автор вже був відкритий
    #             if author['id'] in id_list:
    #                 author_object = find_user_by_id(user_list, author['id'])
    #             # Якщо так, то ми дістаємо старого автора
    #                 # author_object = user_list.
    #             # Якщо ні, то ми створюємо нового автора та зберігаємо
    #             else:
    #                 new_user = User(author['first_name'], author['last_name'], author['phone_number'])
    #                 new_user.id = author['id']
    #                 user_list.append(new_user)
    #                 id_list.append(new_user.id)
    #             # Перевірити чи отримувач вже був відкритий
    #                 # Якщо так, то ми дістаємо старого отримувача
    #                 # Якщо ні, то ми створюємо нового отримувача та зберігаємо
    @classmethod
    def load_json_file(cls):
        id_list = []
        user_list = []
        result_messages = []
        with open(MESSAGES_FILE, 'r') as json_file:
            json_list = json.load(json_file)
            for message in json_list:
                author = message['author']
                recepient = message['recepient']

                author_object = None
                recepient_object = None

                if author['id'] in id_list:
                    author_object = find_user_by_id(user_list, author['id'])
                else:
                    author_object = User(author['first_name'], author['last_name'], author['phone_number'])
                    author_object.id = author['id']
                    user_list.append(author_object)
                    id_list.append(author_object.id)
                if recepient['id'] in id_list:
                    recepient_object = find_user_by_id(user_list, author['id'])
                else:
                    recepient_object = User(author['first_name'], author['last_name'], author['phone_number'])
                    recepient_object.id = author['id']
                    user_list.append(recepient_object)
                    id_list.append(recepient_object.id)

                result_messages.append(Message(
                    message["message_text"],
                    author_object,
                    recepient_object
                ))

        return cls(result_messages)
                
            

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


def find_user_by_id(user_list: list[User], id: int) -> User:
    for user in user_list:
        if user.id == id:
            return user
    raise KeyError(f"No user with id {id}")       
# def user_to_json(user: User)

user_one = User("Ihor", "Last name", "1234567890")
user_two = User("Jane", "Last name", "0987654321")

user_three = User("Jane", "Last name", "0987654321")

message_one = Message("Hello", user_one, user_two)
message_two = Message("Hello, Ihor", user_two, user_one)
message_three = Message("How are you doing?", user_one, user_two)

message_four = Message("TODO: clean the dishes", user_one, user_one)

# print(message_two.to_json())

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
message_system.save_to_file()

new_message_system = MessageSystem.load_json_file()
print(new_message_system)
# print(message_system.find_all_chats(user_one))
# print(message_system.find_all_messages(user_one, user_two))

# my_set = {}
# print(type(my_set))

# with open(MESSAGES_FILE, 'r') as json_file:
#     print(json.load(json_file))
