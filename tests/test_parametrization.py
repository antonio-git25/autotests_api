import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 2, -1])
def test_numbers(number):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1,1), (2,4), (3,9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("host", ["http://dev.comp.ru", "http://stab.comp.ru", "http://prod.comp.ru"])
def test_multiplication_of_numbers(os: str, host: str):
    assert len(os + host) > 0


@pytest.fixture(params=[
    "http://dev.comp.ru",
    "http://stab.comp.ru",
    "http://prod.comp.ru"
])
def host(request: SubRequest) -> str:
    return request.param

def test_host(host: str):
    print(f"Running test on host: {host}")


@pytest.mark.parametrize("user", ["Alice", "Zara"])
class TestOperations:
    def test_user_with_operations(self, user: str):
        print(f"User with operations: {user}")

    def test_user_without_operations(self, user: str):
        print(f"User without operations: {user}")


@pytest.mark.parametrize(
    "cell",
    ["+79601813069","+79101234578","+79634521252"],
    ids=[
    "Fake user",
    "Rich user",
    "Problem user"
])
def test_identifiers_1(cell: str):
    pass


users = {
    "+79601813069": "Fake user",
    "+79101234578": "Rich user",
    "+79634521252": "Problem user"
}
@pytest.mark.parametrize(
    "phone_number",
    users.keys(),  # Передаем список номеров телефонов
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"  # Генерируем идентификаторы динамически
)
def test_identifiers_2(phone_number: str):
    pass



@pytest.mark.parametrize(
    "value",
    [1, pytest.param(2, marks=pytest.mark.skip(reason="Not supported")), 3]
)
def test_example(value):
    pass


@pytest.mark.parametrize(
    "input_value",
    [
        pytest.param(1, marks=pytest.mark.xfail(reason="Known issue with 1")),
        2,
        pytest.param(3, marks=pytest.mark.skip(reason="Feature not implemented for 3")),
    ]
)
def test_function(input_value):
    assert input_value != 1