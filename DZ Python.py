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
d = int(input('число a:'))
f = int(input('число b:'))
g = int(input('число c:'))
numbers = [d, f, g]
numbers.sort()
print(''.join(map(str, numbers)))

                                                    # Задание 8
# Сложно не понимаю








                                                      #Задание 9
import calendar
year = int(input("Введите год: "))
month = int(input("Введите номер месяца (1-12): "))

days_in_month = calendar.monthrange(year, month)[1]

print(f"В {month} месяце {year} года — {days_in_month} дней.")

                                                       #Задание 10

age = int(input("Введите возраст посетителя: "))
time = input("Введите время сеанса в формате ЧЧ:ММ: ")

hours, minutes = map(int, time.split(":"))
time_in_hours = hours + minutes / 60

if age < 3:
    price = 0
elif 3 <= age <= 12:
    price = 10
else:
    price = 15

if time_in_hours <= 12:
    price *= 0.8

print(f"Стоимость билета: ${price:.2f}")