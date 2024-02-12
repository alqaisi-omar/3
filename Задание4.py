# Запрос числа у пользователя
num = int(input("Введите число: "))

# Проверка числа на простоту
is_prime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

# Вывод результата
if is_prime:
    print(num, "является простым числом.")
else:
    print(num, "не является простым числом.")
