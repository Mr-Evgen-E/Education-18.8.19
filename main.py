try:
    countTiсkets = int(input("Введите количество билетов: "))
    sumCost = 0

    for i in range(countTiсkets):
        age = int(input(f"Введите возраст человека (цифрами) {i+1}: "))
        if 0 < age < 110:
            if 18 <= age < 25:
                sumCost += 990
            elif age >= 25:
                sumCost += 1390
        else:
            print("Вы указали неправильный возраст! Повторите оформление заново.")
            sumCost = 0
            break

    if i+1 > 3:
        sumCost = sumCost * 0.9
        print(f"Стоимость билетов, с учетом 10% скидки,  составит: {sumCost} руб.")
    else:
        print(f"Стоимость билетов составит: {sumCost} руб.")

except:
    print("Ошибка! Введите целые числа!!! Повторите оформление заново.")
