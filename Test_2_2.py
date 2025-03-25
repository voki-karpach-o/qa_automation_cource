from Test_2_1 import BasicCalc


class MemoryCalc(BasicCalc):
    def __init__(self):
        self.last_result = 0

    def calc_add(self, first, second=None):
        if second is None:
            second = self.last_result
        result = first + second
        self.last_result = result
        print(result)

    def calc_subtract(self, first, second=None):
        if second is None:
            second = self.last_result
        result = first - second
        self.last_result = result
        print(result)

    def calc_multiply(self, first, second=None):
        if second is None:
            second = self.last_result
        result = first * second
        self.last_result = result
        print(result)

    def calc_divide(self, first, second=None):
        if second is None:
            second = self.last_result
        result = first / second
        self.last_result = result
        print(result)


operations = {
    '+': MemoryCalc.calc_add,
    '-': MemoryCalc.calc_subtract,
    '*': MemoryCalc.calc_multiply,
    '/': MemoryCalc.calc_divide
}

operation = None


calc = MemoryCalc()

num_2 = input("Введите второе число или Enter для использования памяти числа из памяти: ")


calc.calc_add(2)
