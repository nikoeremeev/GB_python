min_limit = 0
max_limit = 10
while True:
    print('Введи число между', max_limit, 'и', max_limit, '?')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('неверно')
    else:
        break
print('Было ввведено число ', num)