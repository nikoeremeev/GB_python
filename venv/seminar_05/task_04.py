"""
✔ Создайте генератор чётных чисел от нуля до 100.
✔ Из последовательности исключите
числа, сумма цифр которых равна 8.
✔ Решение в одну строку.
"""

# def parity_for_number(num):
#     summ = 0
#     while num != 0:
#         summ += num % 10
#         num //= 10
#     if summ % 8 == 0:
#         return True
#     else:
#         return False
#
#
# gen = [i for i in range(0, 100) if not parity_for_number(i) and i % 2 != 0]
# print(gen)
gen = [i for i in range(0, 100) if i % 2 != 0 and sum(list(map(int, str(i)))) % 8 != 0]
print(gen)
