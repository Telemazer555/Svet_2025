def number_sum():
    n = int(input("Введите число: "))
    print('Числа :', end=' ')
    total = 0
    for i in range(n+1):
        print(i, end=' ')
        total += i # эквивалентно `total = total + i`
    print('\nСумма чисел :', total)

number_sum()


