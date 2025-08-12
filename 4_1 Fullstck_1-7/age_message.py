def age_message():
    age = int(input("Введите год вашего рождения: "))
    age = 2025 - age
    print("Ваш возраст: ", age)
    if age < 18:
        print("Вы еще молоды, учеба — ваш путь!")
    # elif age > 18 and age < 65: А можно так было бы записать
    elif 18 < age < 65:
        print("Отличный возраст для карьерного роста!")
    elif age >= 65:
        print("Пора наслаждаться заслуженным отдыхом!")
    else:
        print("Ух ты и так бывает!")


age_message()
