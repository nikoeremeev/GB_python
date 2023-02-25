'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа
используйте код:
    from random import randint
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPT = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)
attempt = 1
number = int(input(f"Введите число (дается {MAX_ATTEMPT} попыток): "))
while attempt <= MAX_ATTEMPT:
    if number < num:
        print("Введенное число меньше загаданного.")
    elif number > num:
        print("Введенное число больше загаданного.")
    else:
        print(f"Вы угадали, загаданное число было {num}.")
        break
    number = int(input(f"Введите число (осталось {MAX_ATTEMPT - attempt} попыток): "))
    attempt += 1
else:
    print(f"Попытки закончились! Загаданное число было {num}.")