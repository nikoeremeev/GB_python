"""
Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
"""

import json


def input_data() -> (str, int, int):
    in_data = input("Введите имя пользователя, идентификатор и уровень доступа через запятую: ").replace(' ', '').split(
        ',')
    return (in_data[0], int(in_data[1]), int(in_data[2])) if len(in_data) == 3 else False


def check_id(data_dict: dict, id: int) -> bool:
    for _, item in data_dict.items():
        for key in item.keys():
            if id in item.keys() or str(id) in item.keys():
                print("Идентификатор не уникален!")
                return True
    return False


def check_level(level: int) -> bool:
    if 0 < level < 8:
        return True
    else:
        print("Уровень доступа может быть от 1 до 7!")
        return False


def add_info(file_name: str = "task_02_data.json") -> None:
    info_dict = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        info_dict = json.load(f)
    print(info_dict)
    while True:
        data = input_data()
        if not data:
            break
        elif not check_id(info_dict, data[1]) and check_level(data[2]):
            if str(data[2]) not in info_dict.keys():
                info_dict[str(data[2])] = {str(data[1]): data[0]}
            else:
                if str(data[1]) not in info_dict[str(data[2])].keys():
                    info_dict[str(data[2])][str(data[1])] = data[0]
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(info_dict, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    # with open("task_02_data.json", 'w', encoding='utf-8') as f:
    #     json.dump({10: {"name": 1111111111}}, f)
    add_info("task_02_data.json")
