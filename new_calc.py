from basic_calc import BasicCalc
import re


class NewCalc(BasicCalc):

    def __init__(self):
        super().__init__()
        self.memory = []

    def memo_plus(self, number=None):
        if len(self.memory) < 3:
            return self.memory.append(number)
        else:
            raise MemoryError("Все ячейки памяти заполнены!")

    def memo_minus(self):
        if self.memory:
            removed = self.memory.pop()
            print(f'Удалено значение: {removed}')
        else:
            raise ValueError("Значений в памяти нет!")

    @property
    def top_memory(self):
        if len(self.memory) > 0:
            return self.memory[-1]
        else:
            raise IndexError("Список пуст!")

    def check_and_calculate_result(self):
        match = re.fullmatch(self.pattern, self.num_1)
        if match:
            first_num, _, operation, second_num, _ = match.groups()
            first_num = float(first_num)
            second_num = float(second_num)
            calculated_result = self.operations[operation](first_num, second_num)
            print(calculated_result)
            self.flag_expression = True
            self.last_result = calculated_result
            return calculated_result

        for n in self.num_1:
            n.replace('.', '', 1)
            if n.isalpha() or n == '.':
                raise ValueError("Введено неправильное значения для первого числа!")

            if len(self.num_1) > 1 and ' ' in self.num_1:
                self.num_1 = [int(n) for n in self.num_1]
                self.flag_sp = True

            else:
                self.num_1 = float(self.num_1)

        if self.flag_sp is False:
            for n in self.num_2:
                n.replace('.', '', 1)
                if n.isalpha() or n == '.':
                    raise ValueError("Введено неправильное значения для первого числа!")

                else:
                    self.num_2 = float(self.num_2)

        if self.flag_expression is False:
            if self.flag_sp:
                calculated_result = self.operations[self.operation](self.num_1)
            else:
                calculated_result = self.operations[self.operation](self.num_1, self.num_2)

            print(calculated_result)
            self.last_result = calculated_result
            return calculated_result


if __name__ == '__main__':
    calc = NewCalc()
    calc.input_info()

    try:
        result = calc.check_and_calculate_result()
        if result is not None:
            print(f"Итоговый результат: {result}")
    except MemoryError as m:
        print(f"Произошла непредвиденная ошибка: {m}")
    except ValueError as v:
        print(f"Произошла непредвиденная ошибка: {v}")
    except IndexError as i:
        print(f"Произошла непредвиденная ошибка: {i}")
