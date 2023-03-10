"""
✔ Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки.
"""


# def str_sort(user_string):
#     user_string.sort()
#     max_len_temp = 0
#     for item in user_string:
#         if len(item) > max_len_temp:
#             max_len_temp = len(item)
#     for i, k in enumerate(user_string, start=1):
#         print(f'{i} {k:>{max_len_temp}}')


# user_string = input("Введите строку:").split()
# str_sort(user_string)

def str_sort(user_string) -> None:
    user_string.sort()
    max_len = len(max(user_string, key=len))
    for i, k in enumerate(user_string, start=1):
        print(f'{i} {k:>{max_len}}')


str_sort("Напишите функцию, которая принимает строку текста".split())
