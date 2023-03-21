"""
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""

from random import randint
from string import ascii_lowercase

MIN_LENGTH = 4
MAX_LENGTH = 7
ABC_LIST = ascii_lowercase
VOWELS = 'aeiou'


def create_psevdo_name(file_name: str = "data.txt") -> None:
    name = []
    vowels_flag = False
    for i in range(randint(MIN_LENGTH, MAX_LENGTH + 1)):
        symbol = ABC_LIST[randint(0, len(ABC_LIST) - 1)]
        if symbol in VOWELS:
            vowels_flag = True
        name.append(symbol)
    if not vowels_flag:
        name[randint(0, len(name))] = VOWELS[randint(0, len(VOWELS) - 1)]
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f"{''.join(name).capitalize()}\n")


if __name__ == '__main__':
    create_psevdo_name("task_02_data.txt")
