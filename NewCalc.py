from basic_calc import BasicCalc
import re


class NewCalc(BasicCalc):
    memory = []

    @staticmethod
    def log_operation(operation_type, arguments, result):
        log_entry = {
            "Операция": operation_type,
            "Аргументы": arguments,
            "Результат": result
        }
        with open("calculator_log.txt", "a", encoding="utf-8") as log_file_op:
            log_file_op.write(str(log_entry) + "\n")

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
                    raise ValueError('Ожидалось "добавить" или "не добавлять"')
            except ValueError as ve:
                print(f'Ошибка: {ve}. Повторите ввод.')

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
                    raise ValueError('Значений в памяти нет!')
            except ValueError as ve:
                print(f'Ошибка: {ve} Повторите ввод!')

    def reset_flags(self):
        self.flag_expression = False
        self.flag_sp = False

    @property
    def top_memory(self):
        if len(self.memory) > 0:
            return self.memory[-1]
        else:
            return 'Список пуст!'

    def check_input(self):
        match = re.fullmatch(self.pattern, self.num_1)
        if match:
            first_num, _, operation, second_num, _ = match.groups()
            first_num = float(first_num)
            second_num = float(second_num)
            res = self.operations[operation](first_num, second_num)
            print(res)
            self.flag_expression = True
            self.last_result = res
            BasicCalc.last_result = res
            return res

        while True:
            for n in self.num_1:
                n.replace('.', '', 1)
                if n.isalpha() or n == '.':
                    print(f'Некорректное значение "{self.num_1}", заменено на 0')
                    self.num_1 = '0'
                    break

            if len(self.num_1) > 1 and ' ' in self.num_1:
                self.num_1 = [int(n) for n in self.num_1.split()]
                self.flag_sp = True
                break
            else:
                self.num_1 = float(self.num_1)
                break

        while True:
            if self.flag_sp is False:
                for n in self.num_2:
                    n.replace('.', '', 1)
                    if n.isalpha() or n == '.':
                        print(f'Некорректное значение "{self.num_2}", заменено на 0')
                        self.num_2 = '0'
                        break

                self.num_2 = float(self.num_2)
                break


calc = NewCalc()

while True:
    start_off_value_input = input('Введи "Начать или Продолжить" чтобы начать или продолжить, "Выйти" чтобы выйти, "Значение", '
                                  'чтобы вывести верхнее значение: ').strip().upper()

    if start_off_value_input in ('ПРОДОЛЖИТЬ', 'НАЧАТЬ'):
        try:
            calc.set_info()
            calc.check_input()
            operation_result = calc.calculate_result()
            calc.log_operation(calc.operation, (calc.num_1, calc.num_2), operation_result)
            calc.memo_plus(operation_result)
            calc.memo_minus()
        except Exception as ex:
            with open("calculator_log.txt", "a", encoding="utf-8") as log_file_err:
                log_file_err.write(str({"Ошибка": str(ex)}) + "\n")

    elif start_off_value_input == 'ВЫЙТИ':
        break
    elif start_off_value_input == 'ЗНАЧЕНИЕ':
        print(calc.top_memory)
    else:
        print('Введите только "ON", "OFF" или "Значение"!')
