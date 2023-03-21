"""
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
"""

import json


def parse_file_to_JSON(file_name: str, file_name_JSON: str) -> None:
    with open(file_name, 'r', encoding='utf-8') as f:
        data_dict = {}
        for line in f:
            lst = line.replace('\n', '').replace(' ', '').split(',')
            data_dict[lst[0].capitalize()] = int(lst[1]) if '.' not in lst[1] else float(lst[1])
        with open(f"{file_name_JSON}.json", 'w', encoding='utf-8') as f1:
            json.dump(data_dict, f1, ensure_ascii=False, indent=2)


parse_file_to_JSON("task_01_data.txt", "task_01_data")
