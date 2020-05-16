# 1) ================================================================================
# Вариант 1
def my_func(n_1, n_2):
    try:
        n_1, n_2 = int(n_1), int(n_2)
    except ValueError:
        return ("Это не число!!! Начните заново")
    while n_2 == 0:
        n_2 = int(input("Введите делитель: "))
    else:
        n_3 = int(n_1) / int(n_2)
        return n_3


print(my_func(input("Введите делимое: "), input("Введите делитель: ")))


# Вариант 2 --------------------------------------------------------------
def my_func(n_1, n_2):
    try:
        n_1, n_2 = int(n_1), int(n_2)
        n_3 = n_1 / n_2
    except ValueError:
        return ("Это не число!!! Начните заново.")
    except ZeroDivisionError:
        return ("На ноль делить нельзя! Начните заново.")
    return n_3


print(my_func(input("Введите делимое - "), input("Введите делитель - ")))


# 2) ================================================================================

def my_data(**kwargs):
    return kwargs


print(my_data(name=input("Your name - "), surname=input("Your surname - "), birth=input("Your year of birth - "),
              city=input("Your city - "), email=input("Your email - "), phone=input("Your mobile - ")))


# 3) ================================================================================

def my_func():
    my_func = (int(input('a = ')), int(input('b = ')), int(input('c = ')))
    return my_func


my_func = list(my_func())
min(my_func)
my_func.remove(min(my_func))
sum(my_func)
print('Сумма наибольших аргументов = ', sum(my_func))


# 4) ================================================================================

def my_func(x, y):
    try:
        x, y = float(x), int(y)
    except ValueError:
        return ("Это не число!!! Начните заново")
    while y >= 0:
        y = int(input('Введите целое отрицательное число y = '))
    else:
        return (f"{1 / x ** abs(y):.10f}")


print(my_func(input('Введите число x = '), input('Введите целое отрицательное число y = ')))

# 5) ================================================================================

# 6) ================================================================================

def int_func(a):
    b, c = [], []
    a.split(' ')
    for el in a.split(' '):
        b.append(el.capitalize())
    c = ' '.join(b)
    return c

print(int_func(input('Введите строку: ')))