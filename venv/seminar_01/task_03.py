'''
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на
школьной тетрадке.
'''
first_num = 2
while first_num < 10:
    second_num = 2
    while second_num <= 10:
        print(f"{first_num} * {second_num} = {first_num * second_num}")
        second_num += 1
    print()
    first_num += 1
