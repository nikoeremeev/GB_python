name = 'Nick'
age = None

a = 45
print(id(a))
a = 'hello world'
print(id(a))
a = 3.14 / 3
print(id(a))

print(name, age, a, 101, 'text', sep=' * ', end='#')
print('any text')

res = input("Print your text: ")
print('Ты написал:', res)

age = int(input('Сколько тебе лет? '))
print(age)

age = float(input('Ваш возраст: '))
how_old = age - 18
print(how_old, "лет назад ты стал совершеннолетним")
