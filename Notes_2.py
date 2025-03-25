import re


class BasicCalc:
    last_result = 0
    pattern = r'^(\d+(\.\d+)?)([+\-*/])(\d+(\.\d+)?)$'

    def __init__(self):
        self.flag_expression = False
        self.flag_letters = False
        self.flag_dot = False
        self.flag_sp = False

    @staticmethod
    def calc_multiply(first, second=None):
        if second is None:
            second = BasicCalc.last_result
        s = first * second
        print(s)
        BasicCalc.last_result = s

    @staticmethod
    def calc_divide(first, second=None):
        if second is None:
            second = BasicCalc.last_result
        s = first / second
        print(s)
        BasicCalc.last_result = s

    @staticmethod
    def calc_subtract(first, second=None):
        if second is None:
            second = BasicCalc.last_result
        s = first - second
        print(s)
        BasicCalc.last_result = s

    @staticmethod
    def calc_add(first, second=None):
        if second is None:
            if isinstance(first, (list, tuple)):
                s = sum(first)
            else:
                s = first + BasicCalc.last_result
        else:
            s = first + second
        print(s)
        BasicCalc.last_result = s

    operations = {
        '+': 'calc_add',
        '-': 'calc_subtract',
        '*': 'calc_multiply',
        '/': 'calc_divide'
    }

    def run(self):
        num_2 = None
        while True:
            num_1 = input('Введи цифру или математическое выражение без пробелов: ')
            match = re.fullmatch(BasicCalc.pattern, num_1)

            if match:
                first_num, _, operation, second_num, _ = match.groups()
                first_num = float(first_num) if '.' in first_num else int(first_num)
                second_num = float(second_num) if '.' in second_num else int(second_num)
                getattr(BasicCalc, BasicCalc.operations[operation])(first_num, second_num)
                self.flag_expression = True
                break
            else:
                if not num_1.replace('.', '', 1).isdigit() and ' ' not in num_1:
                    print('Недопустимая операция!')
                    continue
                if len(num_1) > 1 and ' ' in num_1:
                    num_1 = [int(n) for n in num_1.split()]
                    self.flag_sp = True
                    break
                elif '.' in num_1:
                    num_1 = float(num_1)
                    break
                else:
                    num_1 = int(num_1)
                    break

        if self.flag_expression is False:
            while True:
                self.operation = input('Выберите знак математической операции: +, -, *, /  ')
                if self.operation not in self.operations:
                    print('Недопустимая операция!')
                    continue
                else:
                    break

            if self.flag_sp is False:
                while True:
                    num_2 = input('Введи цифру (или Enter для значения из памяти): ')
                    if num_2 == '':
                        num_2 = None
                        break
                    elif not num_2.replace('.', '', 1).isdigit():
                        print('Недопустимая операция!')
                        continue
                    elif '.' in num_2:
                        num_2 = float(num_2)
                        break
                    else:
                        num_2 = int(num_2)
                        break

        if self.flag_expression is False:
            if self.flag_sp:
                getattr(BasicCalc, self.operations[self.operation])(num_1)
            else:
                getattr(BasicCalc, self.operations[self.operation])(num_1, num_2)


calc = BasicCalc()
while True:
    exit_input = input('Напиши "ON" чтобы начать или продолжить, или "OFF" чтобы выйти: ').strip().upper()
    if exit_input == 'ON':
        calc.run()
    elif exit_input == 'OFF':
        break
    else:
        print('Введите только "ON" или "OFF"')
