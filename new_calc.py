from basic_calc import BasicCalc


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
