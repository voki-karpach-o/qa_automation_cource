import re


class BasicCalc:
    pattern = r'^(\d+(\.\d+)?)([+\-*/])(\d+(\.\d+)?)$'

    def __init__(self):
        self.flag_expression = False
        self.flag_sp = False
        self.num_1_invalid = False
        self.num_2_invalid = False
        self.operation = None
        self.num_1 = None
        self.num_2 = None
        self.pattern = BasicCalc.pattern
        self.last_result = None

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

    def set_info(self):
        self.num_1 = input('Введи цифру или математическое выражение без пробелов: ')
        self.operation = input('Выберите знак математической операции: +, -, *, /  ')
        self.num_2 = input('Введи цифру: ')

    def check_input(self):
        match = re.fullmatch(self.pattern, self.num_1)
        if match:
            first_num, _, operation, second_num, _ = match.groups()
            first_num = float(first_num)
            second_num = float(second_num)
            result = self.operations[operation](first_num, second_num)
            print(result)
            self.flag_expression = True
            self.last_result = result
            return result

        try:
            for n in self.num_1:
                n.replace('.', '', 1)
                if n.isalpha() or n == '.':
                    self.num_1_invalid = True
                    raise ValueError

                if len(self.num_1) > 1 and ' ' in self.num_1:
                    self.num_1 = [int(n) for n in self.num_1]
                    self.flag_sp = True

                else:
                    self.num_1 = float(self.num_1)

        except ValueError:
            print(f'Некорректное значение "{self.num_1}"')

        try:
            if self.flag_sp is False:
                for n in self.num_2:
                    n.replace('.', '', 1)
                    if n.isalpha() or n == '.':
                        self.num_2_invalid = True
                        raise ValueError

                    else:
                        self.num_2 = float(self.num_2)

        except ValueError:
            print(f'Некорректное значение "{self.num_2}"')

    def calculate_result(self):
        if self.flag_expression is False and not self.num_1_invalid and not self.num_2_invalid:
            if self.flag_sp:
                result = self.operations[self.operation](self.num_1)
            else:
                result = self.operations[self.operation](self.num_1, self.num_2)

            print(result)
            self.last_result = result
            return result


if __name__ == '__main__':
    calc = BasicCalc()
    calc.set_info()
    calc.check_input()
    calc.calculate_result()
