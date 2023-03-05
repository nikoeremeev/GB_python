"""
 В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку.

"""

text = input("Введите текст: ").lower() \
    .replace(',', '').replace('.', '').replace('!', '').replace('?', '').split(' ')
my_dict = dict()
for item in text:
    if item not in my_dict.keys():
        my_dict[item] = 1
    else:
        my_dict[item] += 1
my_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
l = 10
if len(my_dict) <= 10:
    l = len(my_dict)
print(my_dict)
for i in range(l):
    print(list(my_dict)[i], end=' ')
