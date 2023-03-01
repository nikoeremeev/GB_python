"""
Создайте в переменной data список значений разных типов перечислив их через
запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты.
"""

import sys

data = [1, 'text', 3.14, True]
flag_int = False
flag_str = False
for item in data:
    if isinstance(item, int):
        if item > 0:
            flag_int = True
        else:
            flag_int = False
    elif isinstance(item, str):
        flag_str = True
        flag_int = False
    else:
        flag_str = False
        flag_int = False

    print(data.index(item), item, id(item), sys.getsizeof(item), hash(item), flag_int, flag_str)
