from basic_calc import BasicCalc


class NewCalc(BasicCalc):
    memory = []

    @staticmethod
    def memo_plus(number=None):
        if len(NewCalc.memory) < 3:
            return NewCalc.memory.append(number)
        else:
            print('Все ячейки памяти заполнены, новые значения не будут сохраняться!')

    @staticmethod
    def memo_minus():
        if NewCalc.memory:
            removed = NewCalc.memory.pop()
            print(f'Удалено значение: {removed}')
        else:
            return 'Значений в памяти нет!'

    def reset_flags(self):
        self.flag_expression = False
        self.flag_sp = False

    @property
    def top_memory(self):
        if len(self.memory) > 0:
            return self.memory[-1]
        else:
            return 'Список пуст!'


if __name__ == "__main__":
    calc = NewCalc()
    calc.memo_plus(BasicCalc.last_result)

    while True:
        start_off_value_input = input(
            'Введи "Продолжить" чтобы продолжить, "Выйти" чтобы выйти, "Значение", '
            '"Удалить" чтобы удалить последнее значение: ').strip().upper()

        if start_off_value_input == 'ПРОДОЛЖИТЬ':
            calc.set_info()
            result = calc.check_input()

            if result is not None:
                calc.memo_plus(result)
            else:
                result = calc.calculate_result()
                calc.memo_plus(result)
        elif start_off_value_input == 'УДАЛИТЬ':
            calc.memo_minus()
        elif start_off_value_input == 'ВЫЙТИ':
            break
        elif start_off_value_input == 'ЗНАЧЕНИЕ':
            print(calc.top_memory)
        else:
            print('Введите только "Продолжить", "Удалить", "Выйти" или "Значение"!')
