import requests

url = "http://ipwho.is/"
response = requests.get(url)

print("HTTP-код статуса ответа:", response.status_code)
print("Текстовое содержимое ответа:", response.text)
print("Содержимое ответа в виде байтов:", response.content)
print("Заголовки HTTP:", response.headers)
print("Кодировка ответа:", response.encoding)
print("Исходный URL-адрес запроса:", response.url)
print("Время выполнения запроса:", response.elapsed)
print("Куки, возвращаемые сервером:", response.cookies)
print("История перенаправлений:", response.history)
print("Запрос успешен (коды 2xx):", response.ok)
print("Сообщение статуса HTTP:", response.reason)

json_response = response.json()
print("Десериализованный JSON-ответ:", json_response)

