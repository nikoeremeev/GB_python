"""
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""


def calc_finance(fin_dict):
    flag = True
    for key, value in fin_dict.items():
        if sum(value) < 0:
            flag = False
        fin_dict[key] = sum(value)
    if flag:
        return True
    else:
        return False


print(calc_finance({'asd': [150, 500, -200], 'abc': [150, 500, -200], 'cab': [850, 500, -200]}))
