"""
Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня.
"""

from math import *
from random import *
import cmath

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
c = int(input("Введите число C: "))

D = b ** 2 - 4 * a * c
print(f"Дискриминант D = {round(D, 2)}" % D)

if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print(f"x1 = {x1}; x2 = {x2}")
elif D == 0:
    x = -b / (2 * a)
    print(f"x = {x1}")
else:
    x1 = (-b + cmath.sqrt(D)) / (2 * a)
    x2 = (-b - cmath.sqrt(D)) / (2 * a)
    print(f"x1 = {x1}; x2 = {x2}")
