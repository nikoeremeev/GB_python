"""Задание №4
Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
    возврат строки без изменений
    возврат строки с преобразованием регистра без потери
    символов
    возврат строки с удалением знаков пунктуации
    возврат строки с удалением букв других алфавитов
    возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
"""

import pytest
import re


def clean_text(text: str) -> str:
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower()


def test_no_change():
    assert clean_text("hello world") == 'hello world', 'no_change'


def test_registr():
    assert clean_text("Hello World") == 'hello world', 'registr'


def test_no_punctuation():
    assert clean_text("Hello, World.") == 'hello world', 'punctuation'


def test_language():
    assert clean_text("Hello World. Привет") == 'hello world ', 'language'


def test_all():
    assert clean_text("Hello World.! Привет") == 'hello world ', 'all'


if __name__ == '__main__':
    pytest.main(['-vv'])
