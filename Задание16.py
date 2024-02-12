# Запрос числа у пользователя
num = int(input("Введите число: "))

# Проверка числа на кратность 3 и 5
if num % 3 == 0 and num % 5 == 0:
    print(num, "кратно и 3, и 5.")
elif num % 3 == 0:
    print(num, "кратно 3.")
elif num % 5 == 0:
    print(num, "кратно 5.")
else:
    print(num, "не кратно ни 3, ни 5.")
