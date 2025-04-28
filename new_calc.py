from basic_calc import BasicCalc


class NewCalc(BasicCalc):
    memory = []

    @staticmethod
    def memo_plus(number=None):
        try:
            if len(NewCalc.memory) < 3:
                return NewCalc.memory.append(number)
            else:
                raise ValueError
        except ValueError:
            print('Все ячейки памяти заполнены, новые значения не будут сохраняться!')

    @staticmethod
    def memo_minus():
        try:
            if NewCalc.memory:
                removed = NewCalc.memory.pop()
                print(f'Удалено значение: {removed}')
            else:
                raise ValueError
        except ValueError:
            print('Значений в памяти нет!')

    @property
    def top_memory(self):
        if len(self.memory) > 0:
            return self.memory[-1]
        else:
            return 'Список пуст!'


if __name__ == "__main__":
    calc = NewCalc()

    while True:
        start_off_value_input = input(
            'Введи "Начать" или "Продолжить" чтобы начать или продолжить, "Выйти" чтобы выйти, "Значение", '
            '"Удалить" чтобы удалить последнее значение: ').strip().upper()

        if start_off_value_input == 'ПРОДОЛЖИТЬ' or start_off_value_input == 'НАЧАТЬ':
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
