from const_data import BASE_URL
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class TestBookings:

    def test_get_all_booking_200(self, auth_session):
        get_all_booking = auth_session.get(f'{BASE_URL}/booking')
        data = get_all_booking.json()
        assert get_all_booking.status_code == 200
        assert isinstance(data, list)
        for item in data:
            assert isinstance(item, dict), f'это чёт уже не словарь {item}'
            for key, value in item.items():
                assert isinstance(value, int), f'не ну это не ИНТ{value}'
                assert "bookingid" in item, f'нету ключа bookingid в словаре {item}'

    def test_create_booking_200(self, booking_data, auth_session):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID букинга не найден в ответе"
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200

        booking_data_response = get_booking.json()
        assert booking_data_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert booking_data_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert booking_data_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert booking_data_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert booking_data_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert booking_data_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении букинга с ID {booking_id}"

        get_deleted_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_deleted_booking.status_code == 404, "Букинг не был удален"

    def test_put_booking_200(self, booking_data, auth_session):

        put_booking = auth_session.put(f'{BASE_URL}/booking/331', json=booking_data)
        assert put_booking.status_code == 200
        put_booking_response = put_booking.json()
        assert put_booking_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert put_booking_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert put_booking_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert put_booking_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert put_booking_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert put_booking_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

    def test_put_booking_none_400(self, booking_data, auth_session):
        booking_data['firstname'] = None
        put_booking = auth_session.put(f'{BASE_URL}/booking/331', json=booking_data)
        assert put_booking.status_code == 400, f'Тест должен был упасть'

    def test_put_booking_int_firstname_200(self, booking_data, auth_session):
        booking_data['firstname'] = 123
        put_booking = auth_session.put(f'{BASE_URL}/booking/331', json=booking_data)
        assert put_booking.status_code == 200, f'По идее он должен не падать и 200 приходить почему 500 хз'
        put_booking_response = put_booking.json()
        assert put_booking_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert put_booking_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert put_booking_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert put_booking_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert put_booking_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert put_booking_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

    def test_patch_booking_200(self, booking_data, auth_session):
        booking_data['firstname'] = None
        patch_booking = auth_session.patch(f'{BASE_URL}/booking/331', json=booking_data)
        assert patch_booking.status_code == 200
        patch_booking_response = patch_booking.json()
        assert patch_booking_response['firstname'] == booking_data['firstname'], "Имя не совпадает с заданным"
        assert patch_booking_response['lastname'] == booking_data['lastname'], "Фамилия не совпадает с заданной"
        assert patch_booking_response['totalprice'] == booking_data['totalprice'], "Цена не совпадает с заданной"
        assert patch_booking_response['depositpaid'] == booking_data['depositpaid'], "Статус депозита не совпадает"
        assert patch_booking_response['bookingdates']['checkin'] == booking_data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert patch_booking_response['bookingdates']['checkout'] == booking_data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"

    def test_patch_booking_one_attribute_200(self, auth_session):
        booking_data_one = {
            "firstname": 323
        }
        get_all_booking = auth_session.get(f'{BASE_URL}/booking/331')
        data = get_all_booking.json()
        patch_booking = auth_session.patch(f'{BASE_URL}/booking/331', json=booking_data_one)
        assert patch_booking.status_code == 200
        patch_booking_response = patch_booking.json()
        assert patch_booking_response['firstname'] == booking_data_one['firstname'], "Имя не совпадает с заданным"
        assert patch_booking_response['lastname'] == data['lastname'], "Фамилия не совпадает с заданной"
        assert patch_booking_response['totalprice'] == data['totalprice'], "Цена не совпадает с заданной"
        assert patch_booking_response['depositpaid'] == data['depositpaid'], "Статус депозита не совпадает"
        assert patch_booking_response['bookingdates']['checkin'] == data['bookingdates'][
            'checkin'], "Дата заезда не совпадает"
        assert patch_booking_response['bookingdates']['checkout'] == data['bookingdates'][
            'checkout'], "Дата выезда не совпадает"
