"""
Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.
"""

init_lst = [5, 7, 8, 6, 9, 10, 2, 5, 5, 4, 6, 7, 8]
dub_lst = []
res = []
for item in init_lst:
    if init_lst.count(item) > 1:
        dub_lst.append(item)
    else:
        res.append(item)
print(f"Список дублирующихся элементов: {dub_lst}")
print(f"Результирующий список: {res}")
