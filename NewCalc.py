from basic_calc import BasicCalc


class NewCalc(BasicCalc):
    memory = []

    @staticmethod
    def memo_plus(number=None):
        while True:
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
                print('Вы ввели неправильный текст!')

    @staticmethod
    def memo_minus():
        while True:
            remove_number = input(
                'Если нужно убрать последнее число, напиши "убрать", '
                'если не нужно убирать то напиши "не убирать" ').lower()
            if remove_number == 'убрать' and len(NewCalc.memory) > 0:
                NewCalc.memory.pop()
                break
            elif remove_number == 'не убирать':
                break
            else:
                print('Значений в памяти нет!')
                break

    def reset_flags(self):
        self.flag_expression = False
        self.flag_sp = False

    @property
    def top_memory(self):
        if len(self.memory) > 0:
            return self.memory[-1]
        else:
            return 'Список пуст!'


calc = NewCalc()
calc.memo_plus(BasicCalc.last_result)
calc.memo_minus()

while True:
    start_off_value_input = input('Введи "Продолжить" чтобы продолжить, "Выйти" чтобы выйти, "Значение", '
                                  'чтобы вывести верхнее значение: ').strip().upper()

    if start_off_value_input == 'ПРОДОЛЖИТЬ':
        calc.set_info()
        calc.check_input()
        result = calc.calculate_result()
        calc.memo_plus(result)
        calc.memo_minus()
    elif start_off_value_input == 'ВЫЙТИ':
        break
    elif start_off_value_input == 'ЗНАЧЕНИЕ':
        print(calc.top_memory)
    else:
        print('Введите только "ON", "OFF" или "Значение"!')
