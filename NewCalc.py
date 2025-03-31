from basic_calc import BasicCalc
import re


class NewCalc(BasicCalc):
    memory = []

    def __init__(self):
        self.flag_expression = False
        self.flag_sp = False
        self.operation = None

    @staticmethod
    def calc_multiply(first, second=None):
        if second is None:
            second = BasicCalc.last_result
        s = first * second
        print(s)
        BasicCalc.last_result = s
        NewCalc.memo_plus(s)
        NewCalc.memo_minus()

    @staticmethod
    def calc_divide(first, second=None):
        if second is None:
            second = BasicCalc.last_result
        s = first / second
        print(s)
        BasicCalc.last_result = s
        NewCalc.memo_plus(s)
        NewCalc.memo_minus()

    @staticmethod
    def calc_subtract(first, second=None):
        if second is None:
            second = BasicCalc.last_result
        s = first - second
        print(s)
        BasicCalc.last_result = s
        NewCalc.memo_plus(s)
        NewCalc.memo_minus()

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
        NewCalc.memo_plus(s)
        NewCalc.memo_minus()

    @staticmethod
    def memo_plus(number=None):
        while True:
            try:
                add_number = input(
                    'Если нужно добавить число, напиши "добавить", если не надо то напиши "не добавлять" ').lower()
                if add_number == 'добавить' and len(NewCalc.memory) < 3:
                    NewCalc.memory.append(number)
                    break
                elif add_number == 'добавить' and len(NewCalc.memory) == 3:
                    print('Невозможно добавить, сейчас уже 3 значения в памяти!')
                    break
                elif add_number == 'не добавлять':
                    break
                else:
                    raise ValueError('ожидалось "добавить" или "не добавлять"')
            except ValueError as e:
                print(f'Ошибка: {e}. Повторите ввод.')

    @staticmethod
    def memo_minus():
        while True:
            try:
                remove_number = input(
                    'Если нужно убрать последнее число, напиши "убрать", '
                    'если не нужно убирать то напиши "не убирать" ').lower()
                if remove_number == 'убрать' and len(NewCalc.memory) > 0:
                    NewCalc.memory.pop()
                    break
                elif remove_number == 'не убирать':
                    break
                else:
                    raise ValueError('значений в памяти нет!')
            except ValueError as e:
                print(f'Ошибка: {e} Повторите ввод!')

    def reset_flags(self):
        self.flag_expression = False
        self.flag_sp = False

    @property
    def top_memory(self):
        if len(self.memory) > 0:
            return self.memory[-1]
        else:
            return 'Список пуст!'

    operations = {
        '+': 'calc_add',
        '-': 'calc_subtract',
        '*': 'calc_multiply',
        '/': 'calc_divide'
    }

    def run(self):
        self.reset_flags()
        num_2 = None
        while True:
            num_1 = input('Введи цифру или математическое выражение без пробелов: ')
            match = re.fullmatch(BasicCalc.pattern, num_1)

            if match:
                try:
                    first_num, _, operation, second_num, _ = match.groups()
                    first_num = float(first_num) if '.' in first_num else int(first_num)
                    second_num = float(second_num) if '.' in second_num else int(second_num)
                    getattr(self.__class__, self.operations[operation])(first_num, second_num)
                    self.flag_expression = True
                    break
                except ZeroDivisionError:
                    print("Ошибка: Деление на ноль! Повторите ввод.")
                    continue
            else:
                if len(num_1) > 1 and ' ' in num_1:
                    try:
                        num_1 = [int(n) for n in num_1.split()]
                        self.flag_sp = True
                        break
                    except ValueError:
                        print(f'Некорректное значение "{num_1}", заменено на 0')
                        num_1 = [0]
                        self.flag_sp = True
                        break
                else:
                    try:
                        num_1 = float(num_1)
                        break
                    except (ValueError, TypeError):
                        print(f'Некорректное значение "{num_1}", заменено на 0')
                        num_1 = 0
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
                    try:
                        if num_2 == '':
                            num_2 = None
                            break
                        elif num_2.count('.') <= 1:
                            num_2 = float(num_2)
                            break
                    except (ValueError, TypeError):
                        print(f'Некорректное значение "{num_2}", заменено на 0')
                        num_2 = 0
                        break

        if self.flag_expression is False:
            try:
                if self.flag_sp:
                    getattr(self.__class__, self.operations[self.operation])(num_1)
                else:
                    getattr(self.__class__, self.operations[self.operation])(num_1, num_2)
            except ZeroDivisionError:
                print("Ошибка: Деление на ноль! Повторите операцию.")
                return


calc = NewCalc()
while True:
    start_off_value_input = input('Введи "Продолжить" чтобы продолжить, "Выйти" чтобы выйти, "Значение", '
                                  'чтобы вывести верхнее значение: ').strip().upper()
    if start_off_value_input == 'ПРОДОЛЖИТЬ':
        calc.run()
    elif start_off_value_input == 'ВЫЙТИ':
        break
    elif start_off_value_input == 'ЗНАЧЕНИЕ':
        print(calc.top_memory)
    else:
        print('Введите только "ON", "OFF" или "Значение"!')
