"""
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""

data = input("Введите данные: ")
if data.isdigit():
    if int(data) > 0:
        print(int(data))
elif data.replace('.', '').replace('-', '').isdigit():
    print(float(data))
else:
    a = True
    for item in data:
        if item in data.upper():
            print(data.lower())
            a = False
            break
    if a:
        print(data.lower())
