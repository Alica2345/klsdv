class InvalidAgeError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Person:
    def __init__(self, name):
        self.name = name
        self.age = None

    def set_age(self, age):
        if age < 0 or age > 120:
            raise InvalidAgeError("Некоректний вік: вік має бути в діапазоні від 0 до 120.")
        self.age = age

try:
    person = Person("Даша")
    age = int(input("Введите вік: "))
    person.set_age(age)
    print(f"вік встановлен: {person.age}")
except InvalidAgeError as e:
    print(f"Помилка: {e}")