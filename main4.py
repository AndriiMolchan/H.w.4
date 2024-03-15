# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class CustomException(Exception):
    def __init__(self, message="Це спеціальний виняток"):
        self.message = message
        super().__init__(self.message)


def f1(value):
    if value == 0:
        raise CustomException("Виняток спеціального значення з f1")


try:
    input_value = int(input("Введіть значення: "))
    f1(input_value)
except CustomException as e:
    print("Помилка:", e.message)
except ValueError as e:
    print("Помилка вводу числа:", e)
else:
    print("Програма відпрацювала без винятків")


