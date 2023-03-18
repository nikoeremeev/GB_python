"""
Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
"""

__all__ = [
    'guess_the_riddle'
]


def guess_the_riddle(riddle: str, variants_of_guesses: list, number_of_attempts: int) -> int:
    print(f"Загадка: {riddle}.")
    for i in range(number_of_attempts):
        answer = input("Введите ответ на загадку: ").lower()
        if answer in variants_of_guesses:
            return i + 1
    return 0


if __name__ == '__main__':
    rid = "Зимой и летом одним цветом."
    variants = ["ель", "сосна"]
    number = 2
    print(guess_the_riddle(rid, variants, number))
