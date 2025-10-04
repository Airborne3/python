
#                                              Задача № 1

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
            print("Делить на ноль нельзя!")
    else:
        print("Неверный номер операции.")
        return
calculator()

#                                              Задача № 2
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

try:
    print("Поиск простых чисел в заданном диапазоне")
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    if start > end:
        print("Ошибка: Начало диапазона не может быть больше конца.")
    else:
        prime_numbers = find_primes_in_range(start, end)
        print(f"\nПростые числа в диапазоне от {start} до {end}:")
        print(prime_numbers)
except ValueError:
    print("Ошибка: Введите целые числа.")