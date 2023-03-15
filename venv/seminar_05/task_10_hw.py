"""
 Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def fib(number):
    fib1, fib2 = 0, 1
    for i in range(number):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


print(*fib(50))
