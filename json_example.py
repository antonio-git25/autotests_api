import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)  # Преобразуем JSON-строку в Python-объект (dict)
print(parsed_data["name"])  # Выведет: Иван

print('\n')
with open("data_pull.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Загружаем JSON из файла
    print(data)
    print(data["age"])
    print(data["courses"])
    print(data["address"]["city"])


with open("data_push.json", "w", encoding="utf-8") as file:
    json.dump(parsed_data, file, indent=4, ensure_ascii=False)


user_data = {
    "name": "Иван Иванов",
    "age": 30,
    "is_active": True,
    "courses": ["Python", "Git"],
    "passport": None
}
with open("data_push_2.json", "w", encoding="utf-8") as file:
    json.dump(user_data, file, indent=4, ensure_ascii=False)