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
        s = first * second
        print(s)
        BasicCalc.last_result = s

    @staticmethod
    def calc_divide(first, second=None):
        s = first / second
        print(s)
        BasicCalc.last_result = s

    @staticmethod
    def calc_subtract(first, second=None):
        s = first - second
        print(s)
        BasicCalc.last_result = s

    @staticmethod
    def calc_add(first, second=None):
        if second is None:
            s = sum(first)
            print(s)
            BasicCalc.last_result = s
        else:
            s = first + second
            print(s)
            BasicCalc.last_result = s

    operations = {
        '+': calc_add,
        '-': calc_subtract,
        '*': calc_multiply,
        '/': calc_divide
    }

    def run(self):
        while True:
            num_1 = input('Введи цифру или математическое выражение без пробелов: ')
            match = re.fullmatch(BasicCalc.pattern, num_1)

            if match:
                first_num, _, operation, second_num, _ = match.groups()
                first_num = float(first_num) if '.' in first_num else int(first_num)
                second_num = float(second_num) if '.' in second_num else int(second_num)
                self.operations[operation](first_num, second_num)
                self.flag_expression = True
                break
            else:
                # проверка на наличие букв
                for n in num_1:
                    n.replace('.', '', 1)
                    if n.isalpha():
                        self.flag_letters = True
                        break
                    elif n == '.':
                        self.flag_dot = True
                        break
                if self.flag_letters is True or self.flag_dot is True:
                    print('Недопустимая операция!')
                    self.flag_letters = False
                    self.flag_dot = False
                    continue
                else:
                    if len(num_1) > 1 and ' ' in num_1:
                        num_1 = [int(n) for n in num_1.split()]
                        self.flag_sp = True
                        break
                    elif '.' in num_1:
                        num_1 = float(num_1)
                        break
                    elif '.' not in num_1:
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
                        num_2 = input('Введи цифру: ')
                        # проверка на наличие букв
                        for n in num_2:
                            n.replace('.', '', 1)
                            if n.isalpha():
                                self.flag_letters = True
                                break
                            elif n == '.':
                                self.flag_dot = True
                                break
                        if self.flag_letters is True or self.flag_dot is True:
                            print('Недопустимая операция!')
                            self.flag_letters = False
                            self.flag_dot = False
                            continue
                        else:
                            if '.' in num_2:
                                num_2 = float(num_2)
                                break
                            elif '.' not in num_2:
                                num_2 = int(num_2)
                                break

            if self.flag_expression is False:
                if self.flag_sp:
                    self.operations[self.operation](num_1)
                else:
                    self.operations[self.operation](num_1, num_2)


calc = BasicCalc()

while True:
    exit_input = input('Напиши "ON" в любом регистре, если хочешь начать использовать калькулятор или "OFF" в любом регистре, если хочешь завершить использование калькулятора').upper()
    if exit_input == 'ON':
        calc.run()
    elif exit_input == 'OFF':
        break
    else:
        print('Введите что-то из предложенного')
        continue


