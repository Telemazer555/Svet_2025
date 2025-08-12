def greet_user():
    name = input('Введите имя:')
    print(f'Привет {name}! Добро пожаловать в мир Питона')


def calculate_sum():
    a = int(input("Введите первое число:"))
    b = int(input("Введите второе число:"))
    return print(f'Сумма чисел:{a + b} ')


if __name__ == '__main__':
    greet_user()
    calculate_sum()
