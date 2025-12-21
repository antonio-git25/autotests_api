import httpx

login_payload = {
    "email": "user123@example.com",
    "password": "123456"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
headers_payload = {"Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"}

me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers_payload)
me_response_data = me_response.json()
print("Refresh response:", me_response_data)
print("Status Code:", me_response.status_code)

