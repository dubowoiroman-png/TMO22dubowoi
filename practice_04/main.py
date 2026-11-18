#Вариант №5

print("Задание 1. Область видимости")
x = 15

def show():
    x = 5
    print(x)

show()
print(x)

#Внутри функции есть локальный x = 5, он используется только при вызове функции и выводится при show(),
#но есть и глобальный x = 15 который будет использоваться при любом ином выводе x.

print("Задание 2. args")
def total(*args):
    return sum(args)

print(total(5, 6, 7))

print("Задание №3. kwargs")

def person(**kwargs):
    name = kwargs.get("name", "Гость")
    age = kwargs.get("age", 0)
    return name, age

print(person(name="Лена", age=21))

print('Задание №4.Функция как параметр')

def increase(x):
    return x + 5

def apply(func, value):
    return func(value)

print(apply(increase, 2))

print('Задание №5. Рекурсия ')

def countdown(n):
    if n == 0:
        return 
    print(n)
    countdown(n - 1)

countdown(2)

