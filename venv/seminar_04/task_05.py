"""
✔ Функция принимает на вход три списка одинаковой длины:
    ✔ имена str,
    ✔ ставка int,
    ✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии.
"""


def calc_bonus_amount(lst_names, lst_rates, lst_bonuses):
    result = dict()
    for i in range(len(lst_names)):
        result[lst_names[i]] = lst_rates[i] * float(lst_bonuses[i].replace('%', ''))
    return result


# def calc_bonus_amount(names: list[str], salaries: list[int], bonus: list[str]) -> dict[str, float]:
#     result = {}
#     for n, s, b in zip(names, salaries, bonus):
#         result[n] = (s * float(b[:-1])) / 100
#     return result


print(calc_bonus_amount(["Вася", "Петя", "Вова"], [1000, 500, 250], ["10.02%", "5.8%", "25%"]))
