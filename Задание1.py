# Запрос чисел у пользователя
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Сравнение чисел и вывод наибольшего
if a > b:
    print("Наибольшее число:", a)
elif b > a:
    print("Наибольшее число:", b)
else:
    print("Числа равны.")
