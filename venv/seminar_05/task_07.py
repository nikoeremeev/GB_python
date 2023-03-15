"""
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def gen_num(num: int) -> int:
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            yield i


my_iter = iter(gen_num(200))
print(next(my_iter))
print(next(my_iter))
