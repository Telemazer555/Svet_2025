def user_input():
    # Запрашивает у пользователя ввод значения и возвращает его
    value_input = (input('Введите значение: '))
    return value_input


def transfer_value_int(data):
    # Пытается преобразовать введенное значение в целое число
    try:
        return int(data)
    except ValueError:
        # Если преобразование не удалось, выводит сообщение об ошибке и возвращает None
        return None


def xvalilka_user():
    # Получает введенное пользователем значение
    value = user_input()
    number = transfer_value_int(value)
    if number is not None and number > 10:
        print("Отличная работа!")
    else:
        print("Попробуйте улучшить результат.")


if __name__ == '__main__':
    # Запускает функцию xvalilka_user, если скрипт запущен напрямую
    xvalilka_user()
