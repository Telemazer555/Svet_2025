def test_case():
    case = []
    while True :
        add_case = input("Сколько тест-кейсов вы выполнили: ") # Ввод числа
        new_case = int(add_case) # Преводим числок к int
        case.append(new_case) # Добовляем в список ввод от пользователя приведённый к int
        if len(case) >= 7: # (Трудоголик бешенный 24/7 лупит не слышал про выходные)
            total = sum(case) #
            average_value = int(total / 7) #
            print(f'Всего выполнено за неделю: {total}') #
            print(f'Среднее количество: {average_value}') #
            break
    if average_value >= 10:
        print("Отличная работа!")
    else:
        print("Попробуйте улучшить результат.")

test_case()
