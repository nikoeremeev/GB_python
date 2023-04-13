"""
Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
📌 загрузка данных (функция из задания 4)
📌 вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из множества пользователей.
📌 добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.
"""

import json
from user_exception import LevelException, AccessException


class User:

    def __init__(self, name: str, id: int, access_level: int):
        self.name = name
        self.id = id
        self.access_level = access_level

    def __hash__(self):
        return hash(self.name)

    # метод проверки на равенство пользователей
    def __eq__(self, other) -> bool:
        return self.id == other.id and self.name == other.name


class Project:
    def __init__(self, user_file) -> None:
        self.users = self.reed_json(user_file)
        self.user = None

    def reed_json(self, file_name):

        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        users = set()

        for access_level, value in data.items():
            for id, name in value.items():
                user = User(name=name, id=id, access_level=access_level)

            users.add(user)
        return users

    def login(self, name: str, id_user: int):
        user = User(name, id_user, access_level=0)
        if user not in self.users:
            raise AccessException
        for u in self.users:
            if u == user:
                return u.access_level

    def add_user(self, user):
        if user.access_level < self.login(user.name, user.id):
            raise LevelException
        self.users.add(user)


project = Project('indent.json')
access_level = project.login('asdf', 12)
new_user = User('Alice', 67890, 1)
project.add_user(new_user)
print('User', new_user.name, 'added successfully')
