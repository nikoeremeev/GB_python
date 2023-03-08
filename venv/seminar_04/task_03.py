"""
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""


def num_unicode(text: str) -> dict[str, int]:
    one, two = map(int, text.split())
    result = {}
    for i in range(min(one, two), max(one, two) + 1):
        result[chr(i)] = i
    return (result)


# print(num_unicode("12 19"))
