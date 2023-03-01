"""
Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""

import math


def area_of_the_circle(diameter):
    return round(1 / 4 * math.pi * diameter ** 2, 42)


def circumference_length(diameter):
    return round(math.pi * diameter, 42)


diameter = int(input(
    "Введите диаметр для вычисления площади круга и длины окружности: "))
while diameter > 1000:
    diameter = int(input(
        "Введите диаметр меньше 1000!: "))
print(f"Площадь круга равна: {area_of_the_circle(diameter)}.")
print(f"Длина окружности равна: {circumference_length(diameter)}.")
