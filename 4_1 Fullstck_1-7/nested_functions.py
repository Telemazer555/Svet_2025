def calculator():
    def nams_function():
        num1 = int(input("Введите первое число:"))
        num2 = int(input("Введите второе число:"))
        return num1, num2

    def input_sign():
        sign = input("Введите знак: +,-,*,/: ")
        return sign

    def return_sign(num1, num2):
        sign = input_sign()
        if sign == "+":
            return Addition(num1, num2)
        elif sign == "-":
            return Subtraction(num1, num2)
        elif sign == "*":
            return Multiplication(num1, num2)
        elif sign == "/":
            return Division(num1, num2)
        else:
            print("Неверный знак!")

    def Addition(num1, num2):
        total = num1 + num2
        return total

    def Subtraction(num1, num2):
        total = num1 - num2
        return total

    def Multiplication(num1, num2):
        total = num1 * num2
        return total

    def Division(num1, num2):
        total = num1 / num2
        return total

    num1, num2 = nams_function()
    result = return_sign(num1, num2)
    print("Результат:", result)


calculator()
