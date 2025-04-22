from basic_calc import BasicCalc
import re


class NewCalc(BasicCalc):
    memory = []

    @staticmethod
    def memo_plus(number=None):
        while True:
            try:
                if len(NewCalc.memory) < 3:
                    return NewCalc.memory.append(number)
                else:
                    raise ValueError
            except ValueError:
                print('Все ячейки памяти заполнены, новые значения не будут сохраняться!')
                break

    @staticmethod
    def memo_minus():
        while True:
            try:
                if NewCalc.memory:
                    removed = NewCalc.memory.pop()
                    print(f'Удалено значение: {removed}')
                else:
                    raise ValueError
            except ValueError:
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


if __name__ == "__main__":
    calc = NewCalc()

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
