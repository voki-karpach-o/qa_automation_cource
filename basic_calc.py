import re


class BasicCalc:
    _instance = None
    pattern = r'^(\d+(\.\d+)?)([+\-*/])(\d+(\.\d+)?)$'

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.operation = None
            self.num_1 = None
            self.num_2 = None
            self.last_result = None
            self.flag_expression = False
            self.pattern = BasicCalc.pattern

            self.operations = {
                '+': self.calc_add,
                '-': self.calc_subtract,
                '*': self.calc_multiply,
                '/': self.calc_divide
            }

    @staticmethod
    def calc_multiply(first, second=None):
        s = first * second
        return s

    @staticmethod
    def calc_divide(first, second=None):
        if second == 0:
            print("Ошибка деления на ноль!")
            return 0
        return first / second

    @staticmethod
    def calc_subtract(first, second=None):
        s = first - second
        return s

    @staticmethod
    def calc_add(first, second=None):
        if second is None:
            return sum(first)
        else:
            return first + second

    def input_info(self):
        self.num_1 = input('Введи цифру или математическое выражение без пробелов: ')
        self.operation = input('Выберите знак математической операции: +, -, *, /  ')
        self.num_2 = input('Введи цифру: ')

    def check_and_calculate_result(self):
        match = re.fullmatch(self.pattern, self.num_1)
        if match:
            first_num, _, operation, second_num, _ = match.groups()
            first_num = float(first_num)
            second_num = float(second_num)
            calculated_result = self.operations[operation](first_num, second_num)
            print(calculated_result)
            self.flag_expression = True
            self.last_result = calculated_result
            return calculated_result

        else:
            try:
                self.num_1 = float(self.num_1)
            except ValueError:
                print(f"Невалидное значение для первого числа ('{self.num_1}')! Заменено на 0.")
                self.num_1 = 0

            try:
                self.num_2 = float(self.num_2)
            except ValueError:
                print(f"Невалидное значение для второго числа ('{self.num_2}')! Заменено на 0.")
                self.num_2 = 0

        if self.flag_expression is False:
            calculated_result = self.operations[self.operation](self.num_1, self.num_2)
            print(calculated_result)
            self.last_result = calculated_result
            return calculated_result


if __name__ == '__main__':
    print("--- Демонстрация Синглтона ---")
    calc_1 = BasicCalc()
    calc_2 = BasicCalc()
    print(f"calc1 это тот же объект, что и calc2? -> {calc_1 is calc_2}")

    calc = BasicCalc()
    calc.input_info()

    try:
        result = calc.check_and_calculate_result()
    except (MemoryError, ValueError, IndexError) as e:
        print(f"Произошла ошибка: {e}")
