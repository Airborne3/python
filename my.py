import math

#                                                  """ 1 занятие по Python """
# from typing import final
# print('Denis')
# print('вторая строка')
# print('привет','мир','пока')
#
# print(55, 33 , 4.4, True)
#
# a=1
# b=2
#
# print(a+b)
# print('Сумма =',a+b)
#
# x=2
# y=5
#
# print(x,'+',y,"=",x+y,)
# print('4','5','6','7',sep='-')
#
# a=17
# print(a)
# a+=1
# print(a)
# a=a-1
#
# print(5/2)
# print(5//2)
# print(5*2)
# print(5**2)
#
# a=4
# b=10
# print('a=',a ,'b=',b)
#
#                                                    """ 2 занятие по Python 26.04.25 """
#
# #a = input('Введите числовое значение: ')
# print(a)
# # #Ввод значения от пользователя и преобразование в целое число
# b= int(input('введите первое значение: '))
# a= int(input('введите второе значение: '))
# print('a=',) # ввод переменной а
# print('b=',)# ввод переменной в
# print('Сумма a+b=',a+b) # вывод суммы
#
# # Целые числа
#
# a=5
# b=0
# d=500000
# e=600_000
# print(a,b,d,e)
#
# # Дробные числа (float)
# a=3.5
# b=0.0
# c=-5.6
# d=50_000.000_03
# e=1.7e2
# print(a,b,c,d,e)
#
# # Логический тип данных
#
# # print(bool(0))
# # print(bool(-1))
# # print(bool(5))
# # print(bool(0.0))
# # print(bool('привет мир'))
# # print(bool(''))
# # print(bool(" "))
#
# # РАВЕНСТВО
#
# print(2==2)
# print(2 =='2')
# print(4<5)
# print(5<=5)
# print(5>=5)
# print(10>=5)
# print(10<=5)
# print(1<5<10)
#
# x=5
# a=1
# b=10
# print(a > x < b)
#
# # СТРОКИ
#
# print("строка в двойных кавычках")
# print('строка в одинарных кавычках')
# print('М.Ю Лермонтов "Бородино"')
# print('М.Ю Лермонтов \'Бородино\'')
#
# # Перенос строк
#
# print('В целом, конечно, курс на социально-ориентированный национальный проект играет \n'
#       'определяющее значение для поэтапного и последовательного развития общества. \n'
#       'Таким образом, внедрение современных методик не даёт нам иного выбора,\n '
#       'кроме определения дальнейших направлений развития. В своём стремлении \n'
#       'повысить качество жизни, они забывают, что граница обучения кадров способствует \n '
#       'подготовке и реализации переосмысления'
#       ' внешнеэкономических политик.')
# print('можно сложить' + ' значение') # стоит пробел сепаратора нет!
# print("можно и так "*3)
#
# print('5'+'5')# строки склеились
# print(5+5)
# #print(5+'5')  # будет ошибка по типу данных
# print(5+int('5'))
# print('5'*3)
# a=5
# b=10
# result =a+b
# print(a,'+', b,'=',result)
# final = str(a),"+" ,str(b), '='+ str (result)
# print(final)
#
# #Списки (List)
#
# list =[ 'привет', 3, 4.4, 454 ]
# print(list)
# print(list[0])
# print(list[0:3])
# print(list[2:9])
#
# print                                              ( ''' 3 занятие по Python 27.04.25 ''')
# # Словари
# myDict={'name':'denis','test':'123',123:'hello'}
# print(myDict.values())
# print(myDict['name'])
#
# # Множества
# mylist = [10,20,30,40,50,10,20]
# myset= set(mylist)
# print(myset)
#
# mylist = ['добрый','Добрый','день','день']
# myset=set(mylist)
# print(myset)
#
# # Преобразование типов данных в Python
#
# a = 5
# a='строка'
# a=[5,5,6]
#
# a=str(a)
# print(a)
#
# x=5.67
# x=int(x)
# print(x)
# print(x+5)
# x=str(x)
# print(x+'строка')
# x=float(x)
# print(x)
#
# a= 'hello!'
# a= list(a)
# print(a)
#
# myTuple=tuple(mylist)
# print(myTuple)
#
# print(chr(5_5_3))
# print(ord('a'))
# print(f'\\u{ord('a'):04x}')
# print(chr(65)) #Таблица кодировок это буква А
#
# # Математические операции с операторами
# a=5
# b=10
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b) # выводит только целый остаток от деления
# print(5%2) # вычисление четного не четного
# print(a**2)
# print(34//4)
# print(5==5)
# print(5!=5)
# print(5>10)
# print(5<10)
# print(5<=10)
#
# # Операторы присвоения
# a +=b
# a -=b
# a *=b
# a **=b
# a /=b
# a //=b
# a %=b
# print(a)

#                                                      """ Занятие по Python 10.05.25 """
# Стандартные математические функции
#
# a = -1 #Functiot abs
# print(abs(a)) # Модуль числа
#
# print(pow(2,10)) # Возведение в степень и нахождение остатка
# print(pow(5,2))
# print(pow(5,-5))
# print(pow(5,2,5))
#
# print(round(1.3,4))  #Округлить до целого
# print(round(4.4678,2)) #Округлить до 2 знаков после запятой
# print(round(4.5,)) # Банковское округление в сторону четного числа
# print(round(5.5,))
# print(round(3.5,))
#
# # Импорт библиотеки функций math
# print('---------')
# math.sqrt(3)
# print(math.ceil(5.7))
# print(math.ceil(5.2))
# print(math.floor(5.8))
# print(math.floor(5.2))
#
# print(math.log(2))

#                                          Практика 11.05.2025

#                                              Задание 1
# num = int(input('Введите день недели'))
# days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
#
# if 1 <= num <= 7:
#     print(days[num - 1])
# else:
#     print("Ошибка: число должно быть от 1 до 7")
#
#                                                 #  Задание 2
# num = int(input('Введите число:'))
# if num % 2 == 0:
#     print("Число является чётным")
# else:
#     print("Число не является чётным")
#                                                    #  Задание 3
# num = int(input('Введите любое число'))
# abs_num = abs(num)
#
# if abs_num < 10:
#     print("Число однозначное")
# elif abs_num < 100:
#     print("Число двузначное")
# elif abs_num < 1000:
#     print("Число трёхзначное")
# else:
#     print("Число не относится к диапазону")
#                                                       #  Задание 4
# age = int(input('Введите свой возраст:'))
# if age >= 18:
#     print("Вам можно голосовать")
# else:
#     print("Вам нельзя голосовать")
                                                       #  Задание 5
# num1 = int(input('число1:'))
# num2 = int(input('число2:'))
# num3 = int(input('число3:'))
# print(max(num1, num2, num3))
# #                                                      Задание 6
# a = int(input('число a:'))
# b = int(input('число b:'))
# c = int(input('число c:'))
# if a == b or a == c or b == c:
#     print("Среди чисел есть одинаковые")
# else:
#     print("Все числа различны")

#                                              Практика за 17.05.2025
# n= 5
# while n<10:
#     print('цикл работает')
#     n += 1
#     if n==1:
#         continue
#     print('Цикл закончился')

#                                              Практика за 18.05.2025
# for x in range (2, 6 ):
#     print(x)
# print('---------')
# for x in range(5,50,5):
#     print(x)
#
# for x,y in enumerate( ['1','2','3']):
#     print(x, '=', y)
#
# ajt=['желтый','синий','зеленый']
# fruits=['банан','цветок','лист']
# for x in ajt:
#     for y in fruits:
#         print((x,y))
#
#  # Задача1
# for number in range(2, 51, 2):
#     print(number)
#
# # Задача2
# n = 100
# sum = n * (n + 1) // 2
# print("Сумма чисел от 1 до 100 равна:", sum)
#
# # Задача3
# def является_простым(n):
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     return True
#
# try:
#     число = int(input("Введите число: "))
#     if является_простым(число):
#         print(f"Число {число} является простым.")
#     else:
#         print(f"Число {число} НЕ является простым.")
# except ValueError:
#     print("Ошибка: введите корректное целое число.")

# # Задача4

# n = int(input('введите число'))
# result = 1
# for i in range (2, n + 1):
#     result *= i
#     print(result)

#                                                Практика за 24.05.25

#                                                  Задача 10

# number =[3,-6,10,0,-3,5,-7]
# result =[]
# for i in number:
#     if abs(i)>5:
#         result.append(i)
# print(result)

#                                                 Практика за 31.05.25
# string = 'Привет мир как у тебя дела? , Все хорошо!'
# print (string.startswith('Привет мир'))
# print (string.endswith('Привет мир'))
# print (string.find('мир'))
# print (string.find('м'))
# print (string.find('Привет'))
# print (string.find('е',1,7))
# print (string.find('е',1))
# print (string.replace('мир','россия'))
# print (string.replace('мир','россия'))
#
# #                                            Задача 1
# user_input = input("Введите строку: ")
# reversed_string = user_input[::-1]
# print("Обратная строка:", reversed_string)
# #                                            Задача 2
# def are_anagrams(str1, str2):
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#
#     return sorted(str1) == sorted(str2)
#
# string1 = input("Введите первую строку: ")
# string2 = input("Введите вторую строку: ")
#
# if are_anagrams(string1, string2):
#     print("Строки являются анаграммами.")
# else:
#     print("Строки не являются анаграммами.")
# #                                            Задача 3
# text = input("Введите строку: ").lower()
# vowels = set('аеёиоуыэюя')
# vowel_count = 0
# consonant_count = 0
# for char in text:
#     if char in vowels:
#         vowel_count += 1
#     elif char.isalpha():
#         consonant_count += 1
# print(f"Количество гласных букв: {vowel_count}")
# print(f"Количество согласных букв: {consonant_count}")
# #                                            Задача 4
# text = input("Введите строку: ").lower()
# cleaned_text = ''.join(char for char in text if char.isalnum())
# if cleaned_text == cleaned_text[::-1]:
#     print("Это палиндром!")
# else:
#     print("Это не палиндром.")
# #                                            Задача 5
# from itertools import permutations
# text = input("Введите строку: ")
# unique_perms = set(permutations(text))
# print("Все уникальные перестановки символов:")
# for p in unique_perms:
#     print(''.join(p))
# #                                            Задача 6
# text = input("Введите строку: ")
# text_without_spaces = text.replace(' ', '')
# print("Строка без пробелов:", text_without_spaces)

#                                       Практика за 01.06.25
# #                                            Задача 7
# text = input("Введите строку: ")
# words = text.split()
# if words:
#     longest_word = max(words, key=len)
#     print("Самое длинное слово:", longest_word)
# else:
#     print("Нет ни одного слова.")
#
# #                                            Задача 8
# import re
# text = input("Введите исходную строку: ")
# old_word = input("Какое слово нужно заменить? ")
# new_word = input("На какое слово заменить? ")
# new_text = re.sub(re.escape(old_word), new_word, text, flags=re.IGNORECASE)
# print("Изменённая строка:", new_text)
# #                                            Задача 9
# text = input("Введите строку: ").lower()
# alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
# letters_in_text = set(char for char in text if char in alphabet)
# if letters_in_text >= alphabet:
#     print("Это панграмма!")
# else:
#     print("Это не панграмма.")

#                                            Задача 10
# text = input("Введите строку: ")
# capitalized_text = ' '.join(word.capitalize() for word in text.split())
# # print("Преобразованная строка:", capitalized_text)
#
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщЪЫЬэюя'
#
# for position in range(11):
#     print('^'*27)
#     for letter in alphabet:
#         if alphabet.index(letter) % 11 == position:
#             print(' |', letter.upper(),letter,' |',end='' )
#     print()
# print('^'*27)
#
#
# #                                                            Практика за 07.06.25
# #                                                             Задача 14
#
# import math
# def get_divisors(n):
#     divisors = set()
#     for i in range(1, int(math.isqrt(n)) + 1):
#         if n % i == 0:
#             divisors.add(i)
#             divisors.add(n // i)
#     return sorted(divisors)
# numbers = [23436, 190187200, 380457890232]
# for num in numbers:
#     print(f"Делители числа {num}:")
#     print(get_divisors(num))
#     print("-" * 40)

 #                                                            Практика за 08.06.25
#
# def print_number_as_dashes():
#     try:
#         n = int(input("Введите число: "))
#         if n < 0:
#             print("Ошибка: введите положительное число.")
#             return
#
#         half = n // 2
#         rest = n - half
#
#         print('-' * half)
#         print('-' * rest)
#
#     except ValueError:
#         print("Ошибка: введите корректное целое число.")
# print_number_as_dashes()

# def print_rengtangle(n):
#     for _ in range (3):
#         print('-'*8)
#
# n = int(input('Введите ширину прямоугольника '))
# print_rengtangle(n)

# def print_triangle(n):
#     for i in range(1,n+1):
#         print('*' * i )
#
# n = int(input('Введите ширину прямоугольника '))
# print_triangle(n)

#                                                            Практика за 14.06.25

#                                                              Задача 8
# def is_prime(n):
#     if n<2: return False
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
# primes = [i for i in]
# Primes=[]
# for i in range(100, 1000):
#     if is_prime(i):
#     primes.append(i)
# print(primes)
#                                                              Задача 9
# number = input("Введите шестизначное число: ")
# if len(number) != 6 or not number.isdigit():
#     print("Ошибка: Введите корректное шестизначное число (без пробелов и букв).")
# else:
#     first_sum = sum(int(digit) for digit in number[:3])
#     second_sum = sum(int(digit) for digit in number[3:])
#     if first_sum == second_sum:
#         print(f"Число {number} — счастливое3")
#     else:
#         print(f"Число {number} не счастливое(.")

 #                                                              Задача 10
# input_str = input("Введите 6 различных целых чисел через пробел: ")
# try:
#     numbers = list(map(int, input_str.split()))
#     if len(numbers) != 6:
#         print("Ошибка: должно быть ровно 6 чисел.")
#     elif len(set(numbers)) != 6:
#         print("Ошибка: все числа должны быть различными.")
#     else:
#         max_number = max(numbers)
#         print(f"Максимальное число: {max_number}")
# except ValueError:
#     print("Ошибка: введите корректные целые числа.")
#
#     #                                                              Задача 14
#     import math
#     def area_circle(radius):
#         return math.pi * radius ** 2
#     def area_rectangle(length, width):
#         return length * width
#     def main():
#         print("Выберите фигуру для вычисления площади:")
#         print("1 - Круг")
#         print("2 - Прямоугольник")
#         choice = input("Введите номер фигуры (1 или 2): ")
#         if choice == '1':
#             radius = float(input("Введите радиус круга: "))
#             print(f"Площадь круга с радиусом {radius} равна: {area_circle(radius)}")
#         elif choice == '2':
#             length = float(input("Введите длину прямоугольника: "))
#             width = float(input("Введите ширину прямоугольника: "))
#             print(f"Площадь прямоугольника с длиной {length} и шириной {width} равна: {area_rectangle(length, width)}")
#         else:
#             print("Неверный выбор. Пожалуйста, введите 1 или 2.")
#
#     if __name__ == "__main__":
#         main()
#                                                                  Задача 16
def draw_square(n, s):
    for i in range(n):
        print(s * n)
def main():
    try:
        n = int(input("Введите размер стороны квадрата: "))
        s = input("Введите символ для рисования квадрата: ")

        if len(s) != 1:
            print("Ошибка: нужно ввести ровно один символ!")
        elif n <= 0:
            print("Ошибка: размер квадрата должен быть положительным числом.")
        else:
            draw_square(n, s)
    except ValueError:
        print("Ошибка: размер квадрата должен быть целым числом.")
if __name__ == "__main__":
    main()
#                                                                Задача 17
