import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)  # Преобразуем JSON-строку в Python-объект (dict)

print(parsed_data["age"])  # Выведет: Иван


def no_pytest_def():
    assert (2 + 2) == 4
    print("assert 1 passed")
    assert (3 + 3) == 7
    print("assert 2 passed")
    assert (4 + 4) == 8
    print("assert 3 passed")

no_pytest_def()