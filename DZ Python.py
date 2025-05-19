#                                                    # домашнее задание 1
#
# result = (2 ** 5 + 10) * 3 - 15
#
# print("Результат выражения:", result)
#
#                                              # Домашнее задание номер 2 за 26.04.25
#
# Запрос данных у пользователя
#
# you_name = input('как вас зовут? ')
# yoy_last_name = input("какая ваша фамилия?") # Это не по заданию просто понравилось тема интересная
# you_age = input("Сколько вам лет?")
# du_you_likes_programming =input('нравится ли вам программировать?')
#
# # Вывод собранных данных
# print(' Это ваши данные :')
# print(f'Фамилия {yoy_last_name}')
# print(f"Имя: {you_name}")
# print(f"Возраст: {you_age}")
# print(f"Вы любите программировать: {du_you_likes_programming}")
#
#                                  #Задание2
#
# # Запрос данных у пользователя
# x = float(input("Введите значение x: "))
# y = float(input("Введите значение y: "))
#
# # Вычисление результата выражения
# result = y > x - 2
#
# # Вывод результата
# print(f"Результат выражения (y > x - 2): {result}")

# Словарь

# person = { "name": you_name, "age": you_age,"любит программировать": du_you_likes_programming }

#                                            ''' Домашнее задание за 10.05.25 '''
# number = int(input('Введите число'))
# if -9 < number < 2:
#     print("Число принадлежит интервалу (-9; 2)")
# else:
#     print("Число не принадлежит интервалу (-9; 2)")

#                                         ''' Домашнее задание за 11.05.25 '''
#                                                  Задания с 7 по 10

                                                     # Задание 7
# d = int(input('число a:'))
# f = int(input('число b:'))
# g = int(input('число c:'))
# numbers = [d, f, g]
# numbers.sort()
# print(''.join(map(str, numbers)))

                                                    # Задание 8

# sales = []
# for i in range(3):
#     sale = float(input(f"Введите объем продаж для менеджера {i+1}: "))
#     sales.append(sale)
#
# def calculate_salary(sales_amount):
#     if sales_amount <= 500:
#         bonus = sales_amount * 0.03
#     elif sales_amount <= 1000:
#         bonus = sales_amount * 0.05
#     else:
#         bonus = sales_amount * 0.08
#     return 200 + bonus
#
# salaries = [calculate_salary(s) for s in sales]
#
# max_sales = max(sales)
# best_indices = [i for i, s in enumerate(sales) if s == max_sales]
#
# if len(best_indices) == 1:
#     best_index = best_indices[0]
#     salaries[best_index] += 200
#
# print("\nИтоговые зарплаты:")
# for i in range(3):
#     print(f"Менеджер {i+1}: ${salaries[i]:.2f} (продажи: ${sales[i]:.2f})")
#
# if len(best_indices) == 1:
#     print(f"\nЛучший менеджер: Менеджер {best_index + 1}, ему начислена премия 200$.")
# else:
#     print("\nНесколько лидеров или нет явного лучшего. Премия не начисляется.")
#
#
#                                                       #Задание 9
# import calendar
# year = int(input("Введите год: "))
# month = int(input("Введите номер месяца (1-12): "))
#
# days_in_month = calendar.monthrange(year, month)[1]
#
# print(f"В {month} месяце {year} года — {days_in_month} дней.")
#
#                                                        #Задание 10
#
# age = int(input("Введите возраст посетителя: "))
# time = input("Введите время сеанса в формате ЧЧ:ММ: ")
#
# hours, minutes = map(int, time.split(":"))
# time_in_hours = hours + minutes / 60
#
# if age < 3:
#     price = 0
# elif 3 <= age <= 12:
#     price = 10
# else:
#     price = 15
#
# if time_in_hours <= 12:
#     price *= 0.8
# print(f'Стоимость билета: ${price:.2f}hours')
#
#                                            Дз  18.05.2025

                                             # Задача5

# def fibonacci (n):
#     последовательность = []
#     a, b = 0, 1
#     for _ in range(n):
#         последовательность.append(a)
#         a, b = b, a + b
#     return последовательность
#
# Result = fibonacci(10)
# print("Первые 10 чисел Фибоначчи:")
# print(Result )
# #                                                    # Задача 6
#
# print("Числа от 10 до 1 в обратном порядке:")
# for i in range(10, 0, -1):
#     print(i)
                                                     # Задача 7
# def подсчет_гласных(строка):
#     гласные = set("аеёиоуэюяАЕЁИОУЭЮЯ")
#     счетчик = 0
#     for символ in строка:
#         if символ in гласные:
#             счетчик += 1
#     return счетчик
# ввод = input("Введите строку на русском языке: ")
# результат = подсчет_гласных(ввод)
#
# print("Количество гласных букв:", результат)
#                                              # Задача 8
def сумма_цифр(число):

    сумма = 0
    for цифра in str(число):
        сумма += int(цифра)
    return сумма

try:
    число = input("Введите целое положительное число: ")
    if not число.isdigit():
        print("Ошибка: введено не целое положительное число.")
    else:
        число = int(число)
        результат = сумма_цифр(число)
        print("Сумма цифр числа:", результат)
except ValueError:
    print("Ошибка: введите корректное число.")
                                              # Задача 10
print("Таблица умножения от 1 до 10:\n")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:3}", end=" ")
    print()
