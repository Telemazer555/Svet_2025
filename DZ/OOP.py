# Базовый класс банковского счёта
import pytest

class BankAccount:
    def __init__(self, owner, balance=0):
        # Конструктор инициализирует владельца счёта и начальный баланс
        self.owner = owner                     # Публичный атрибут — имя владельца
        self.__balance = balance               # Приватный атрибут — баланс, доступен только внутри класса

    def deposit(self, amount):
        # Метод для пополнения счёта
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной")
        self.__balance += amount               # Увеличиваем баланс на переданную сумму

    def withdraw(self, amount):
        # Метод для снятия денег со счёта
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount               # Уменьшаем баланс на сумму снятия

    def get_balance(self):
        # Метод для получения текущего баланса
        return self.__balance                  # Возвращает текущий баланс

# Класс сберегательного счёта
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0):
        # Конструктор инициализирует родительский класс и процентную ставку
        super().__init__(owner, balance)       # Вызываем конструктор базового класса
        self.interest_rate = 0.05              # Устанавливаем фиксированную процентную ставку (5%)

    def apply_interest(self):
        # Метод начисления процентов на текущий баланс
        interest = self.get_balance() * self.interest_rate  # Вычисляем сумму процентов
        self.deposit(interest)                 # Добавляем проценты к балансу

# Класс текущего (расчетного) счёта
class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        # Переопределённый метод, позволяет уходить в минус (овердрафт)
        self._BankAccount__balance -= amount   # Доступ к приватному атрибуту через "name mangling"


savings = SavingsAccount("Артём Голубев")
savings.deposit(500)
savings.withdraw(100)
savings.apply_interest()
print("Текущий баланс:", savings.get_balance())


# def test_deposit_positive_amount():
#     account = BankAccount("Тест Пользователь")
#     account.deposit(100)
#     assert account.get_balance() == 100
#
# def test_deposit_negative_amount_raises():
#     account = BankAccount("Тест Пользователь")
#     with pytest.raises(ValueError, match="Сумма депозита должна быть положительной"):
#         account.deposit(0)
#
#     with pytest.raises(ValueError):
#         account.deposit(-50)
