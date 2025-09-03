def info():
    while True:
        work = (input("Какая у вас работа, qa или aqa?:"))
        if work == 'qa':
            break
        elif work == 'aqa':
            break
        else:
            print("Ассалам алейкум брат, мы попали в блок else ...попробуй снова")
            continue

    while True:
        age = (input("0 = джун, 1 = мидл, 3 = синьёр \nСколько лет работаем в QA ?:"))
        if age == '0':
            st = 'джун'
            break
        elif age == "1":
            st = 'мидл'
            break
        elif age == '3':
            st = 'синьёр'
            break
        else:
            print("Ассалам алейкум брат, мы попали в блок else ...попробуй снова")
            continue

    while True:
        param = (input("Что такое переменная?:"))
        if param == 'Именованные ссылки на объекты, которые хранятся в памяти компьютера':
            break
        elif param == "ыыы":
            break
        elif param == 'xz':
            break
        else:
            print("Ассалам алейкум брат, мы попали в блок else ...попробуй снова")
            continue

    print(f"Ты работаешь в {work}, уже {age} лет, ну ты наверное {st}, ещё и {param}")


info()
