"""
Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
"""

from sys import argv
from random import randint

__all__ = [
    'guess_the_number'
]


def guess_the_number(lower_bound: int = 0, upper_bound: int = 100, number_of_attempts: int = 5) -> bool:
    random_number = randint(lower_bound, upper_bound)
    num = int(input(f"Введите число от {lower_bound} до {upper_bound}: "))
    count = 1
    while count != number_of_attempts:
        if num == random_number:
            return True
        elif num > random_number:
            print("Заданное число меньше!")
        else:
            print("Заданное число больше!")
        num = int(input(f"Введите число (осталось попыток {number_of_attempts - count}): "))
        count += 1
    return False


if __name__ == '__main__':
    temp, *params = argv
    print(guess_the_number(*(int(n) for n in params)))
