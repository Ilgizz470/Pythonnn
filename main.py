print("Представляем нашу команду: Okurmeny")
print("Выберите часть калькулятора:")
print("1️⃣ - Обычный калькулятор")
print("2️⃣ - Калькулятор валют")
print("3️⃣ - Калькулятор массы")

choice = input("Введите 1, 2 или 3: ")

# ========== ЧАСТЬ 1: Обычный калькулятор ==========
if choice == "1":
    print("Первая часть калькулятора 1️⃣")

    print("Операции: +, -, *, /, %, ^")
    op = input("Выберите операцию: ")
    agay = float(input("Введите первое число: "))
    agay2 = float(input("Введите второе число: "))

    if op == "+":
        ans = agay + agay2
        print("Ответ: " + str(ans))

    elif op == "-":
        ans = agay - agay2
        print("Ответ: " + str(ans))

    elif op == "*":
        ans = agay * agay2
        print("Ответ: " + str(ans))

    elif op == "/":
        if agay2 == 0:
            print("Нельзя делить на ноль!")
        else:
            ans = agay / agay2
            print("Ответ: " + str(ans))

    elif op == "%":
        ans = agay * agay2 / 100
        print("Ответ: " + str(ans))

    elif op == "^":
        ans = agay ** agay2
        print("Ответ: " + str(ans))

    else:
        print("Такой операции не существует!")

# ========== ЧАСТЬ 2: Калькулятор валют ==========
elif choice == "2":
    print("Вторая часть калькулятора 2️⃣")
    print("Добро пожаловать в калькулятор валют! 💵")

    print("Курсы валют:")
    print("1 доллар = 88.5 сом")
    print("1 рубль = 1 сом")
    print("1 юань = 12.3 сом")

    print("Доступные валюты: USD, KGS, RUB, CNY")

    from_currency = input("Из какой валюты переводим? ").upper()
    to_currency = input("В какую валюту переводим? ").upper()
    amount = float(input("Сколько переводим? "))

    # Переводим в сомы
    if from_currency == "USD":
        amount_in_kgs = amount * 88.5
    elif from_currency == "RUB":
        amount_in_kgs = amount * 1
    elif from_currency == "CNY":
        amount_in_kgs = amount * 12.3
    elif from_currency == "KGS":
        amount_in_kgs = amount
    else:
        print("Неизвестная валюта!")
        exit()

    # Перевод из сома в нужную валюту
    if to_currency == "USD":
        result = amount_in_kgs / 88.5
    elif to_currency == "RUB":
        result = amount_in_kgs / 1
    elif to_currency == "CNY":
        result = amount_in_kgs / 12.3
    elif to_currency == "KGS":
        result = amount_in_kgs
    else:
        print("Неизвестная валюта!")
        exit()

    print(f"{amount} {from_currency} = {round(result, 2)} {to_currency}")

# ========== ЧАСТЬ 3: Калькулятор массы ==========
elif choice == "3":
    print("Третья часть калькулятора 3️⃣")
    print("Добро пожаловать в калькулятор массы 📏")

    kg = float(input("Введите массу в килограммах: "))

    g = kg * 1000
    t = kg / 1000
    centner = kg / 100
    mg = kg * 1_000_000

    print("Масса:")
    print("Килограммы:", kg, "кг")
    print("Граммы:", g, "г")
    print("Тонны:", t, "т")
    print("Центнеры:", centner, "ц")
    print("Миллиграммы:", mg, "мг")

else:
    print("Неверный выбор!")
