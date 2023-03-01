"""
Напишите программу, которая получает целое
число и возвращает его шестнадцатеричное
строковое представление. Функцию hex
используйте для проверки своего результата.
"""


def convert_to(number, base=16):
    digits = '0123456789abcdef'
    if base > len(digits):
        return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result


num = int(input("Введите число для перевода в hex-формат: "))
print(f"В шестнадцатеричном виде число {num} равно {convert_to(num)}.")
print(hex(num))
