# Запрос года у пользователя
year = int(input("Введите год: "))

# Проверка на високосность
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "год является високосным.")
    days_in_february = 29
else:
    print(year, "год не является високосным.")
    days_in_february = 28

# Вывод количества дней в феврале
print("Количество дней в феврале", year, "года:", days_in_february)
