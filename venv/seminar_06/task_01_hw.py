"""
Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.
"""


def add_riddle(riddle: str, variants_of_guesses: list, dict_of_riddles: dict = {}) -> dict:
    dict_of_riddles[riddle] = variants_of_guesses
    return dict_of_riddles


def guess_the_riddle(riddle: str, variants_of_guesses: list, number_of_attempts: int) -> int:
    print(f"Загадка: {riddle}.")
    for i in range(number_of_attempts):
        answer = input("Введите ответ на загадку: ").lower()
        if answer in variants_of_guesses:
            return i + 1
    return 0


def game_guess(dict_of_riddles: dict, number_of_attempts: int):
    for key, item in dict_of_riddles.items():
        count = guess_the_riddle(key, item, number_of_attempts)
        if count == 0:
            print("Поппытки закончились, переходим к следующей загадке "
                  "или начните игру заново!")
        else:
            print(f"Вы угадали с {count} попыки!")


if __name__ == '__main__':
    rid1 = "Зимой и летом одним цветом."
    variants1 = ["ель", "сосна"]
    rid2 = "Шубка серая для лета, Для зимы — другого цвета."
    variants2 = ["заяц", "зайчик"]
    rid3 = "На колесах едет ловко, если тянешь за веревку."
    variants3 = ["машинка", "машина"]
    number = 5
    dict_og_riddles = add_riddle(rid1, variants1)
    dict_og_riddles = add_riddle(rid2, variants2, dict_og_riddles)
    dict_og_riddles = add_riddle(rid3, variants3, dict_og_riddles)
    game_guess(dict_og_riddles, number)
