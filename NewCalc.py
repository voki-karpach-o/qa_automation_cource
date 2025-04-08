from basic_calc import BasicCalc
import re


class NewCalc(BasicCalc):
    memory = []

    def log_operation(self, operation_type, arguments, result_val):
        log_entry = {
            "Операция": operation_type,
            "Аргументы": arguments,
            "Результат": result_val
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
            except ValueError as val_err_plus:
                print(f'Ошибка: {val_err_plus}. Повторите ввод.')

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
            except ValueError as val_err_minus:
                print(f'Ошибка: {val_err_minus} Повторите ввод!')

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
            first_num, _, op, second_num, _ = match.groups()
            first_num = float(first_num)
            second_num = float(second_num)
            result_expr = self.operations[op](first_num, second_num)
            print(result_expr)
            self.flag_expression = True
            self.last_result = result_expr
            BasicCalc.last_result = result_expr
            self.log_operation("выражение", (first_num, second_num), result_expr)
            return result_expr

        while True:
            for ch in self.num_1:
                ch.replace('.', '', 1)
                if ch.isalpha() or ch == '.':
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
                for ch in self.num_2:
                    ch.replace('.', '', 1)
                    if ch.isalpha() or ch == '.':
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
            result_value = calc.calculate_result()
            if not calc.flag_expression:
                calc.log_operation(calc.operation, (calc.num_1, calc.num_2), result_value)
            calc.memo_plus(result_value)
            calc.memo_minus()
        except Exception as main_err:
            with open("calculator_log.txt", "a", encoding="utf-8") as log_f_err:
                log_f_err.write(str({"Ошибка": str(main_err)}) + "\n")

    elif start_off_value_input == 'ВЫЙТИ':
        break
    elif start_off_value_input == 'ЗНАЧЕНИЕ':
        print(calc.top_memory)
    else:
        print('Введите только "ON", "OFF" или "Значение"!')
