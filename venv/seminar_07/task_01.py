"""
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.
"""

from random import randint
from random import uniform

MIN_LIMIT = -1000
MAX_LIMIT = 1000


def add_random_pair(row_count: int = 1, file_name: str = "task_01_data.txt") -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for i in range(row_count):
            f.write(f"{randint(MIN_LIMIT, MAX_LIMIT)} | {uniform(MIN_LIMIT, MAX_LIMIT)}\n")


if __name__ == '__main__':
    add_random_pair(5)
