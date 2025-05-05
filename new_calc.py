from basic_calc import BasicCalc


class NewCalc(BasicCalc):

    def __init__(self):
        super().__init__()
        self.memory = []

    def memo_plus(self, number=None):
        if len(self.memory) < 3:
            return self.memory.append(number)
        else:
            print('Все ячейки памяти заполнены, новые значения не будут сохраняться!')

    def memo_minus(self):
        if self.memory:
            removed = self.memory.pop()
            print(f'Удалено значение: {removed}')
        else:
            print('Значений в памяти нет!')

    @property
    def top_memory(self):
        if len(self.memory) > 0:
            return self.memory[-1]
        else:
            print('Список пуст!')


if __name__ == "__main__":
    calc = NewCalc()
    calc.input_info()
    result = calc.check_input()

    if result is not None:
        calc.memo_plus(result)

    else:
        result = calc.calculate_result()
        calc.memo_plus(result)
