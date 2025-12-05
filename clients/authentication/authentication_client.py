from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client
from httpx import Response
from typing_extensions import TypedDict


class Token(TypedDict):
    tokenType: str
    accessToken: str
    refreshToken: str

class LoginRequestDict(TypedDict):
    email: str
    password: str

class LoginResponseDict(TypedDict):
    token: Token

class RefreshRequestDict(TypedDict):
    refreshToken: str


class AuthenticationClient(APIClient):
    def login_api(self, request: LoginRequestDict) -> Response:
        """
        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("api/v1/authentication/refresh", json=request)

    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        response = self.login_api(request)
        return response.json()


# Добавляем builder для AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())