# a=5
# b=7
# if a<b:
#     print(a)
#     if a<b:
#         print('а равно б')
#     else:
#         print('а не рвано б'))

#
# cost = 2000
# if cost < 1000:
#     print('cкидки нет')
# if cost < 3000:
#     print('скидка 5%')
# if cost < 5000:
#     print("скидка 7%")
# else:
#     print(' скидка 10%')
#
# if cost < 1000:
#     print('скидки нет')
#     if cost < 3000:
#         print('скидка 5%')
#     else:
#         print('скидка 10%')

# # задание 1
# number =6
# print(number)
# if number > 5:
#     print("это число больше пяти")

# задание 2
# a = int(input('Введите целое число '))
# if a > 0:
#     a += 1
# else:
#     a -= 2
# print(a)

# задание 3
def calculator():
    print("Добро пожаловать в калькулятор!")

    try:
        num1 = float(input("Введите первое число: "))
    except ValueError:
        print("Ошибка: Некорректный ввод первого числа.")
        return


    try:
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: Некорректный ввод второго числа.")
        return


    print("\nВыберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    operation = input("Введите номер операции (1/2/3/4): ")

    if operation == '1':
        result = num1 + num2
        print(f"\nРезультат: {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"\nРезультат: {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"\nРезультат: {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"\nРезультат: {num1} / {num2} = {result}")
        else:
            print("Ошибка: Деление на ноль невозможно!")
    else:
        print("Ошибка: Неверный номер операции.")
        return

calculator()