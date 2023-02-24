MIN_NUM = 1
MAX_NUM = 999

num = int(input(f"Введите число от {MIN_NUM} до {MAX_NUM}: "))

if num < 10:
    print('цифра', f"квадрат цифры {num} - {num ** 2}")
elif 9 < num < 100:
    first_number = num // 10
    second_number = num % 10
    print(f"произведение цифр двухзначного числа {num} равно {first_number * second_number}")
else:
    first_number = num // 100
    second_number = num % 100 // 10
    third_number = num % 10
    print(f"для трехзначного числа {num} зеркальное число равно {third_number * 100 + second_number * 10 + first_number}")

