def announce(func):
    def wrapper():
        print("Начинаем")
        result = func()
        print("Готово")
        return result
    return wrapper

@announce
def hello():
    print("Привет!")

hello()