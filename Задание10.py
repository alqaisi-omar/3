# Запрос трех чисел у пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

# Проверка на равенство трех чисел
if num1 == num2 == num3:
    print("Введенные числа равны между собой.")
else:
    print("Введенные числа не равны между собой.")
