from basic_calc import BasicCalc


class NewCalc(BasicCalc):
    memory = []

    @staticmethod
    def memo_plus(number=None):
        try:
            if len(NewCalc.memory) < 3:
                return NewCalc.memory.append(number)
            else:
                raise MemoryError
        except MemoryError:
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
            raise ValueError('Список пуст!')


if __name__ == "__main__":
    calc = NewCalc()
    calc.set_info()
    result = calc.check_input()

    if result is not None:
        calc.memo_plus(result)

    else:
        result = calc.calculate_result()
        calc.memo_plus(result)
