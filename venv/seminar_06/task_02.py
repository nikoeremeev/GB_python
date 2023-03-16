"""
Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
"""

from random import randint


def guess_the_number(lower_bound, upper_bound, number_of_attempts):
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


guess_the_number(0, 100, 5)
