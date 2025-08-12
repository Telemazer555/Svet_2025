import pytest
from OOP import BankAccount

# def test_deposit_positive_amount():
#     account = BankAccount("Артём Голубев")
#     account.deposit(1000)
#     assert account.get_balance() > 0

def test_deposit_negative_amount_raises():
    account = BankAccount("Артур Голубев")
    account.deposit(100)
    print(account.get_balance())
    # account.
    with pytest.raises(ValueError, match="Сумма депозита должна быть положительной"):
        account.deposit(0)

    with pytest.raises(ValueError,match="Сумма депозита должна быть"):
        account.deposit(-50)
