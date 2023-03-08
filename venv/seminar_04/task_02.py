"""
✔ Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def unicode_for_str(text: str) -> list[int]:
    result = set()
    for char in text:
        result.add(ord(char))
    result = sorted(result, reverse=True)
    return result


print(unicode_for_str(input("Введите текст:")))
