import pytest
from pydantic import BaseModel, ValidationError
from requests import Response
from typing import Type, Optional, Union, Mapping, Any
# from const_data import (BASE_URL,)


class ItemApiClient:
    def __init__(self, auth_session):
        self.auth_session = auth_session
        self.base_url = BASE_URL  # Можно также передавать в конструктор, если он может меняться

    def create_item(self, item_data):
        """Отправляет запрос на создание item."""
        response = self.auth_session.post(f"{self.base_url}booking", json=item_data)
        # Базовая проверка, что запрос успешен и мы можем парсить JSON
        if response.status_code not in (200, 201):
            response.raise_for_status()  # Выбросит HTTPError для плохих статусов
        return response.json()

    def get_items(self):
        """Отправляет запрос на получение списка items."""
        response = self.auth_session.get(f"{self.base_url}/booking")
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    def update_item(self, item_id, upd_item_data):
        """Отправляет запрос на обновление item."""
        response = self.auth_session.put(f"{self.base_url}/booking/{item_id}", json=upd_item_data)
        if response.status_code != 200:
            response.raise_for_status()
        return response.json()

    def delete_item(self, item_id):
        """Отправляет запрос на удаление item."""
        response = self.auth_session.delete(f"{self.base_url}/booking/{item_id}")
        if response.status_code != 200:  # В REST API для DELETE часто возвращают 204 No Content или 200 OK
            response.raise_for_status()
        # Для DELETE часто нечего возвращать из тела, либо можно вернуть статус-код или сам response
        return response  # или response.status_code


class ItemScenarios:
    def __init__(self, api_client: ItemApiClient):  # Типизация для ясности
        self.api_client = api_client

    def create_item_and_immediately_delete(self, item_data):
        """
        Сценарий: создать item и сразу же его удалить.
        Возвращает ID созданного и удаленного item.
        """
        created_item_data = self.api_client.create_item(item_data)
        item_id = created_item_data.get("id")
        assert item_id is not None, f"ID не найден в ответе на создание: {created_item_data}"

        self.api_client.delete_item(item_id)  # Проверка на успешность удаления внутри delete_item (raise_for_status)
        # или можно проверить статус ответа здесь, если delete_item его возвращает
        print(f"Item с ID {item_id} успешно создан и удален.")
        return item_id

    def get_and_verify_items_exist(self):
        """
        Сценарий: получить список items и проверить, что он не пуст.
        """
        items = self.api_client.get_items()
        assert len(items) > 0, "Список items пуст"
        print(f"Получено {len(items)} items.")
        return items

    def update_item_and_verify_changes(self, item_id, upd_item_data):
        """
        Сценарий: обновить item и проверить, что данные изменились.
        """
        updated_item = self.api_client.update_item(item_id, upd_item_data)

        assert updated_item["description"] == upd_item_data["description"], \
            f"Описание не обновилось. Ожидалось: {upd_item_data['description']}, получено: {updated_item['description']}"
        assert updated_item["title"] == upd_item_data["title"], \
            f"Заголовок не обновился. Ожидалось: {upd_item_data['title']}, получено: {updated_item['title']}"
        print(f"Item с ID {item_id} успешно обновлен.")
        return updated_item

    def delete_existing_item_and_verify(self, item_id):  # test_item переименован в item_id для ясности
        """
        Сценарий: удалить существующий item и убедиться, что он удален.
        """
        self.api_client.delete_item(item_id)
        print(f"Item с ID {item_id} отправлен на удаление.")


def validate_response(response: Response,
                      model: Type[BaseModel],
                      expected_status: int = 200,
                      expected_data: dict | None = None
                      ) -> BaseModel:
    if response.status_code != expected_status:
        pytest.fail(f"Expected status {expected_status}, got {response.status_code}: {response.text}")
    try:
        data = response.json()
    except Exception as e:
        pytest.fail(f"Ошибка парсинга JSON: {e}\nResponse: {response.text}")
    try:
        parsed = model(**data)
    except ValidationError as e:
        pytest.fail(f"Pydantic валидация не прошла:\n{e}")
    if expected_data:
        # Обернём данные в такую же модель для сравнения
        expected_model = model(**expected_data)
        if parsed.model_dump(exclude_unset=True) != expected_model.model_dump(exclude_unset=True):
            pytest.fail(
                f"Данные ответа не совпадают с ожидаемыми:\n"
                f"Expected: {expected_model.model_dump()}\n"
                f"Actual:   {parsed.model_dump()}"
            )

    return parsed


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingResponse(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None



import requests
import pytest
from faker.proxy import Faker
# from api_base import ItemApiClient, ItemScenarios
# from const_data import HEADERS, BASE_URL, JSON_BODY

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

@pytest.fixture
def api_client(auth_session):
    return ItemApiClient(auth_session)

@pytest.fixture
def item_scenarios(api_client):
    return ItemScenarios(api_client)


import pytest

# from const_data import BASE_URL
import urllib3
# from const_data import UserSchema
# from api_base import validate_response
# from api_base import  BookingResponse
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# from api_base import  ItemScenarios

class TestBookings:
    def test_create_and_delete_item(self, item_scenarios):
        """Тест создания и немедленного удаления item"""
        test_item_data = {
            "title": "Test Item",
            "description": "Test Description",
            "price": 100,
        }

        item_id = item_scenarios.create_item_and_immediately_delete(test_item_data)
        print(f"Успешно создан и удален item с ID: {item_id}")
        assert item_id is not None

    def test_get_item(self, item_scenarios):
        items = item_scenarios.get_and_verify_items_exist()
        print(f"Получено {len(items)} items")
        assert len(items) > 0
    def test_create_and_delete_item(item_scenarios):
        """Тест создания и немедленного удаления item"""
        # Подготовка тестовых данных
        test_item_data = {
            "title": "Test Item",
            "description": "Test Description",
            "price": 100,
            # добавьте другие необходимые поля
        }

        # Вызов функции
        try:
            item_id = item_scenarios.create_item_and_immediately_delete(test_item_data)
            print(f"Успешно создан и удален item с ID: {item_id}")

            # Дополнительные проверки (опционально)
            assert item_id is not None
            # Можно проверить, что item действительно удален

        except Exception as e:
            pytest.fail(f"Тест не прошел: {e}")

    def test_get_item(item_scenarios):
        item_id = item_scenarios.get_and_verify_items_exist()
        return item_id

    # print(f"Успешно создан и удален item с ID: {test_get_item()}")

HEADERS = {'content-type': 'application/json'}
BASE_URL = 'https://restful-booker.herokuapp.com'
JSON_BODY = {"username":"admin", "password":"password123"}


from pydantic import BaseModel, Field
from typing import Optional



class BookingDates(BaseModel):
    checkin: str
    checkout: str


class UserSchema(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: dict
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None