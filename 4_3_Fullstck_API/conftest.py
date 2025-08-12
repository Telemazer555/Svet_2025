import requests
import pytest
from faker.proxy import Faker

from const_data import HEADERS, BASE_URL, JSON_BODY

fake = Faker()

@pytest.fixture(scope='session')
def auth_session():
    session = requests.session()
    session.headers.update(HEADERS)
    session.verify = False
    auth_response = session.post(f"{BASE_URL}/auth",json=JSON_BODY)
    assert auth_response.status_code == 200, "Ошибка авторизации, статус код не 200"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"
    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture()
def booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Breakfast"
    }
