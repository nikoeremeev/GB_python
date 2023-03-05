"""
Создайте вручную кортеж содержащий элементы разных типов.
✔ Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа. - как сделать для строк список проверку по типу?????
"""

data = (1, "str", 12.32, "abc",)
my_dict = {}
for item in data:
    if type(item) not in my_dict.keys():
        my_dict[type(item)] = item
    else:
        temp = []
        temp.append(my_dict[type(item)])
        print(temp)
        my_dict[type(item)] = temp.append(item)
print(my_dict)
