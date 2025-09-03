def info():
    Triathlon = 300
    # print(f'Этого маловато для троеборья {Triathlon}')
    while True:

        try:
            Squat = (input("Сколько присед?:"))
            if not Squat:
                Squat = 0
            Squat = int(Squat)

            chestpress = (input("Сколько жмёшь?:"))
            if not chestpress:
                chestpress = 0
            chestpress = int(chestpress)

            while True:
                Deadlift = (input("Сколько тянешь?:"))
                if not Deadlift:
                    print('Тянуть надо полюбому')
                else:
                    try:
                        Deadlift = int(Deadlift)
                        break
                    except ValueError:
                        print("НУЖНЫ ЦИФРЫ!!!")
                        continue

        except    ValueError:
            print("Сума сдурел, циферки пиши, давай всё по новой")
            continue

        Triathlon = Squat + chestpress + Deadlift
        print(f'Присед:  {Squat}')
        print(f'Жим:  {chestpress}')
        print(f'Тяга:  {Deadlift}')
        print("Общая сумма троеборья:", Triathlon)

        rembo = 600
        if rembo < Triathlon:
            print('Ну ты точно калгон пьёшь')
            break
        else:
            print(f"Иди качайся лалка, нужно набить: {rembo}")
            break


info()
