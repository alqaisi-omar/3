# Запрос числа у пользователя
num = int(input("Введите число: "))

# Преобразование числа в строку для перебора цифр
num_str = str(num)

# Создание списков для четных и нечетных цифр
even_digits = []
odd_digits = []

# Перебор каждой цифры числа и разделение на четные и нечетные
for digit in num_str:
    digit_int = int(digit)
    if digit_int % 2 == 0:
        even_digits.append(digit_int)
    else:
        odd_digits.append(digit_int)

# Вывод результатов
print("Четные цифры числа:", even_digits)
print("Нечетные цифры числа:", odd_digits)
