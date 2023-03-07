"""
✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка.
"""


def calc_sum(lst_nums, start_index, finish_index):
    if start_index > finish_index:
        start_index, finish_index = finish_index, start_index
    if finish_index >= len(lst_nums):
        finish_index = len(lst_nums)
    if start_index < 0:
        start_index = 0
    result = 0
    for i in range(start_index, finish_index):
        result += lst_nums[i]
    return result


print(calc_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 2))
