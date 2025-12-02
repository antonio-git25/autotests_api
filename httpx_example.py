import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

data = {
  "title": "new task",
  "completed": False,
  "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.request.headers)
print(response.json())


print('\n')
data = {"username": "test_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.request.headers)
print(response.json())


print('\n')
headers = {"Authorization": "Fucker MY dick"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.request.headers)
print(response.json())


print('\n')
params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)
print(response.json())


print('\n')
files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())


print('\n')
try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")
