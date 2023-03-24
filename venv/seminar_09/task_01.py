"""
Создайте функцию-замыкание, которая запрашивает два целых числа:
    от 1 до 100 для загадывания,
    от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
"""

from random import randint

__all__ = [
    'guess_the_number'
]


def guess_the_number(number: int, count: int):
    def wrapper():
        for i in range(1, count + 1):
            print(f"Попытка номер {i} из {count}.")
            user_num = int(input("Введите число от 1 до 100: \n >>> "))
            if user_num == number:
                print("Угадал!!!")
                break
            elif user_num < number:
                print("Ваше число меньше")
            else:
                print("Ваше число больше")

    return wrapper


if __name__ == '__main__':
    temp = guess_the_number(randint(1, 100), randint(1, 10))
    temp()
