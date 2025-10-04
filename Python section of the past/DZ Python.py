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
# def сумма_цифр(число):
#
#     сумма = 0
#     for цифра in str(число):
#         сумма += int(цифра)
#     return сумма
#
# try:
#     число = input("Введите целое положительное число: ")
#     if not число.isdigit():
#         print("Ошибка: введено не целое положительное число.")
#     else:
#         число = int(число)
#         результат = сумма_цифр(число)
#         print("Сумма цифр числа:", результат)
# except ValueError:
#     print("Ошибка: введите корректное число.")
#                                               # Задача 10
# print("Таблица умножения от 1 до 10:  ")
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i * j:3}", end=" ")
#     print()

#                                          Дз 24.05.2025
# Задача 11
# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# cleaned = ''.join([char for char in letters if not char.isupper()])
# print(cleaned)
#
# #Задача 12
#
# secret_list = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", "Клодобродыч"]
#
# nickname = input("Введите ваш никнейм: ")
#
# if nickname in secret_list:
#     print(f"Ты – свой. Приветствую, любезный {nickname}!")
# else:
#     print("Тут ничего нет. Еще есть вопросы?")

#                                          Дз 31.05.2025
#                                             Задача 6
# text = input("Введите строку: ")
# text_without_spaces = text.replace(' ', '')
# print("Строка без пробелов:", text_without_spaces)

#                                             Задача 7
# text = input("Введите строку: ")
# words = text.split()
# if words:
#     longest_word = max(words, key=len)
#     print("Самое длинное слово:", longest_word)
# else:
#     print("Нет ни одного слова.")
#                                          Дз 01.06.2025

# text = input("Введите текст: ")
# vowels = set('аеёиоуыэюяАЕЁИОУЫЭЮЯ')
# vowel_count = 0
# consonant_count = 0
# for char in text:
#     if char.isalpha():
#         if char in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
# words = text.split()
# longest_word = ''
# max_length = 0
# for word in words:
#     cleaned_word = ''.join(c for c in word if c.isalpha())
#     if len(cleaned_word) > max_length:
#         max_length = len(cleaned_word)
#         longest_word = cleaned_word
# search_word = input("Введите слово для поиска: ").lower()
# word_count = 0
# for word in words:
#     cleaned_word = ''.join(c for c in word if c.isalpha()).lower()
#     if cleaned_word == search_word:
#         word_count += 1
# print(f"Гласных букв: {vowel_count}")
# print(f"Согласных букв: {consonant_count}")
# print(f"Самое длинное слово: {longest_word}")
# print(f"Слово '{search_word}' встречается: {word_count} раз(а)")

#                                              Дз 07.06.2025

#                                             Задача 4
# def average(*args: int) -> float:
#     return sum(args) / len(args)
# try:
#     numbers = list(map(int, input("Введите 5 целых чисел через пробел: ").split()))
#     if len(numbers) != 5:
#         print("Ошибка: должно быть ровно 5 чисел.")
#     else:
#         result = average(*numbers)
#         print(f"Среднее арифметическое: {result:.2f}")
# except ValueError:
#     print("Ошибка: введите корректные целые числа.")

#                                             Задача 5
# def count_digits(n: int) -> int:
#     """
#     Возвращает количество цифр в десятичной записи целого числа.
#     """
#     return len(str(abs(n)))
# try:
#     number = int(input("Введите целое число: "))
#     result = count_digits(number)
#     print(f"Количество цифр в числе {number}: {result}")
# except ValueError:
#     print("Ошибка: введите корректное целое число.")

#                                             Задача 7
# import math
# def distance(p1, p2):
#     x1, y1 = p1
#     x2, y2 = p2
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# print("Введите координаты трёх вершин треугольника (по две координаты на точку):")
# x1 = float(input("Координата x точки A: "))
# y1 = float(input("Координата y точки A: "))
# x2 = float(input("Координата x точки B: "))
# y2 = float(input("Координата y точки B: "))
# x3 = float(input("Координата x точки C: "))
# y3 = float(input("Координата y точки C: "))
# A = (x1, y1)
# B = (x2, y2)
# C = (x3, y3)
# ab = distance(A, B)
# bc = distance(B, C)
# ca = distance(C, A)
# perimeter = ab + bc + ca
# print(f"\nДлина AB: {ab:.2f}")
# print(f"Длина BC: {bc:.2f}")
# print(f"Длина CA: {ca:.2f}")
# print(f"Периметр треугольника: {perimeter:.2f}")

#                                              Дз 08.06.2025

# def greet_and_count(user_name: str) -> None:
#     print(f"Привет, {user_name}! Добро пожаловать!")
#     filtered_name = user_name.replace(' ', '')
#     char_count = len(filtered_name)
#     print(f"Количество символов в вашем имени без учета пробелов: {char_count}")
# name = input("Введите ваше имя: ")
# greet_and_count(name)

#                                             Дз от 14.06.2025
#                                              Задача 11
# def swap(x, y):
#     return y, x
# a = 10
# b = 20
# c = 30
# d = 40
# print("До обмена:")
# print(f"a = {a}, b = {b}")
# print(f"c = {c}, d = {d}")
# a, b = swap(a, b)
# c, d = swap(c, d)
# print("\nПосле обмена:")
# print(f"a = {a}, b = {b}")
# print(f"c = {c}, d = {d}")
#                                               Задача 12
# import math
#
# def is_triangle(a, b, c):
#     return a + b > c and a + c > b and b + c > a
# def area(a, b, c):
#     p = (a + b + c) / 2
#     return math.sqrt(p * (p - a) * (p - b) * (p - c))
# print("Введите стороны первого треугольника:")
# a1 = float(input("Сторона a: "))
# b1 = float(input("Сторона b: "))
# c1 = float(input("Сторона c: "))
# print("\nВведите стороны второго треугольника:")
# a2 = float(input("Сторона a: "))
# b2 = float(input("Сторона b: "))
# c2 = float(input("Сторона c: "))
# if not is_triangle(a1, b1, c1):
#     print("\nОшибка: Первый треугольник не существует.")
# elif not is_triangle(a2, b2, c2):
#     print("\nОшибка: Второй треугольник не существует.")
# else:
#     perimeter1 = a1 + b1 + c1
#     perimeter2 = a2 + b2 + c2
#     total_perimeter = perimeter1 + perimeter2
#     area1 = area(a1, b1, c1)
#     area2 = area(a2, b2, c2)
#     total_area = area1 + area2
#     print(f"\nПериметр первого треугольника: {perimeter1}")
#     print(f"Площадь первого треугольника: {area1:.2f}")
#
#     print(f"\nПериметр второго треугольника: {perimeter2}")
#     print(f"Площадь второго треугольника: {area2:.2f}")
#
#     print(f"\nСумма периметров: {total_perimeter}")
#     print(f"Сумма площадей: {total_area:.2f}")

#                                             Дз от 15.06.2025

#                                              Задача 19
# def pointInTriangle(x, y, x1, y1, x2, y2, x3, y3):
#     def cross_product(ax, ay, bx, by, px, py):
#         return (bx - ax) * (py - ay) - (by - ay) * (px - ax)
#     cp1 = cross_product(x1, y1, x2, y2, x, y)
#     cp2 = cross_product(x2, y2, x3, y3, x, y)
#     cp3 = cross_product(x3, y3, x1, y1, x, y)
#     same_sign_positive = cp1 >= 0 and cp2 >= 0 and cp3 >= 0
#     same_sign_negative = cp1 <= 0 and cp2 <= 0 and cp3 <= 0
#
#     return same_sign_positive or same_sign_negative
# print("Введите координаты точки:")
# x_p = float(input("Координата x точки: "))
# y_p = float(input("Координата y точки: "))
# print("\nВведите координаты вершин треугольника:")
# print("Вершина A:")
# x_a = float(input("x A: "))
# y_a = float(input("y A: "))
# print("Вершина B:")
# x_b = float(input("x B: "))
# y_b = float(input("y B: "))
# print("Вершина C:")
# x_c = float(input("x C: "))
# y_c = float(input("y C: "))
#
# result = pointInTriangle(x_p, y_p, x_a, y_a, x_b, y_b, x_c, y_c)
# print(f"\nТочка ({x_p}, {y_p}) находится внутри треугольника ABC — {result}")
#
# #                                              Задача 20
#
# def pointInTriangle(x, y, x1, y1, x2, y2, x3, y3):
#     def cross_product(ax, ay, bx, by, cx, cy):
#         return (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
#     cp1 = cross_product(x1, y1, x2, y2, x, y)
#     cp2 = cross_product(x2, y2, x3, y3, x, y)
#     cp3 = cross_product(x3, y3, x1, y1, x, y)
#     has_same_sign = (cp1 >= 0 and cp2 >= 0 and cp3 >= 0) or (cp1 <= 0 and cp2 <= 0 and cp3 <= 0)
#     return has_same_sign
# print("Введите координаты точки:")
# x = float(input("Координата x: "))
# y = float(input("Координата y: "))
# print("\nВведите координаты трёх вершин треугольника:")
# print("Вершина A:")
# x1 = float(input("x1: "))
# y1 = float(input("y1: "))
# print("Вершина B:")
# x2 = float(input("x2: "))
# y2 = float(input("y2: "))
# print("Вершина C:")
# x3 = float(input("x3: "))
# y3 = float(input("y3: "))
# result = pointInTriangle(x, y, x1, y1, x2, y2, x3, y3)
# print("\nРезультат:", result)
#
# #                                              Задача 21
#
# def calculate_score(score1, score2, score3, score4, score5):
#     scores = [score1, score2, score3, score4, score5]
#     scores_sorted = sorted(scores)
#     middle_scores = scores_sorted[1:-1]
#     average = sum(middle_scores) / len(middle_scores)
#     return average
# print("Введите оценки пяти экспертов (целое число от 0 до 100):")
# scores = []
# for i in range(5):
#     while True:
#         try:
#             score = int(input(f"Оценка эксперта {i + 1}: "))
#             if 0 <= score <= 100:
#                 scores.append(score)
#                 break
#             else:
#                 print("Ошибка! Число должно быть от 0 до 100.")
#         except ValueError:
#             print("Ошибка! Введите целое число.")
# final_score = calculate_score(*scores)
# print("\nИтоговая оценка спортсмена:", round(final_score, 2))

#                                             Дз от 21.06.2025
#                                              Задача 21
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# try:
#     n = int(input("Введите номер числа Фибоначчи (n ≥ 0): "))
#     if n < 0:
#         print("Ошибка: Число должно быть неотрицательным.")
#     else:
#         result = fibonacci(n)
#         print(f"\nЧисло Фибоначчи под номером {n}: {result}")
# except ValueError:
#     print("Ошибка: Введите целое число.")
#                                             Дз от 22.06.2025
#                                              Задача 1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(width=side, height=side)
#         self.side = side
# rect = Rectangle(5, 10)
# print("Прямоугольник:")
# print("Площадь:", rect.area())
# print("Периметр:", rect.perimeter())
# square = Square(4)
# print("\nКвадрат:")
# print("Площадь:", square.area())
# print("Периметр:", square.perimeter())
# print("Сторона квадрата:", square.side)

#                                              Задача 2
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Пол: {self.gender}")


class Employee(Person):
    def __init__(self, name, age, gender, salary, position):
        super().__init__(name, age, gender)
        self.salary = salary
        self.position = position

    def work(self):
        print(f"{self.name} работает как {self.position} с зарплатой {self.salary}.")

employees = []
def main_menu():
    while True:
        print("\n===== Меню =====")
        print("1. Добавить нового сотрудника")
        print("2. Показать список сотрудников")
        print("3. Удалить сотрудника")
        print("4. Выйти")
        choice = input("Выберите действие (1/2/3/4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            show_employees()
        elif choice == '3':
            delete_employee()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")

def add_employee():
    print("\nВведите данные сотрудника:")
    name = input("Имя: ")
    age = input("Возраст: ")
    gender = input("Пол (муж/жен): ")
    salary = input("Зарплата: ")
    position = input("Должность: ")

    try:
        age = int(age)
        salary = float(salary)
        employee = Employee(name, age, gender, salary, position)
        employees.append(employee)
        print(f"\nСотрудник {name} успешно добавлен.\n")
    except ValueError:
        print("Ошибка: Возраст и зарплата должны быть числами.\n")

def show_employees():
    if not employees:
        print("\nСписок сотрудников пуст.")
        return

    print("\n===== Список сотрудников =====")
    for idx, emp in enumerate(employees):
        print(f"\nСотрудник {idx + 1}:")
        emp.introduce()
        emp.work()

def delete_employee():
    if not employees:
        print("\nНет сотрудников для удаления.")
        return
    show_employees()
    try:
        number = int(input("Введите номер сотрудника для удаления: "))
        if 1 <= number <= len(employees):
            removed = employees.pop(number - 1)
            print(f"\nСотрудник {removed.name} удалён.")
        else:
            print("Ошибка: Неверный номер.")
    except ValueError:
        print("Ошибка: Введите корректный номер (число).")
main_menu()