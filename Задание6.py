# Запрос числа у пользователя
num = int(input("Введите число: "))

# Проверка числа на кратность 7
if num % 7 == 0:
    print(num, "кратно 7.")
else:
    print(num, "не кратно 7.")
