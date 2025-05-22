import re
import time
import math
import random
from collections import Counter
from datetime import datetime
from .basic_calc import BasicCalc


class ExecutionTimer:
    def __enter__(self):
        self.start_time = time.time()
        return self.start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        print(f" Время выполнения операции: {duration:.4f} секунд")


def cache_result(func):
    cache = {}

    def wrapper(*args, **kwargs):
        if (args, tuple(kwargs.items())) in cache:
            print("Результат взят из кэша")
            return cache[(args, tuple(kwargs.items()))]
        else:
            calculated_result = func(*args, **kwargs)
            cache[(args, tuple(kwargs.items()))] = calculated_result
            return calculated_result

    return wrapper


@cache_result
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


@cache_result
def factorial_regular(n):
    if n == 0 or n == 1:
        return 1
    return math.factorial(n)


def initialize_factorial_cache(cache, limit=100):
    for i in range(limit + 1):
        cache[(i,)] = factorial_recursive(i)
        print(f"Факториал рекурсивный {i} инициализирован в кэш.")
    for i in range(limit + 1):
        cache[(i,)] = factorial_regular(i)
        print(f"Факториал обыкновенный {i} инициализирован в кэш.")


class NewCalc(BasicCalc):
    def __init__(self):
        super().__init__()
        self.memory = []

    @staticmethod
    def generate_random_numbers():
        random_value = []
        for n in range(100):
            random_value.append(random.randint(0, 100))
        count_value = Counter(random_value)

        for key_value, count_value in count_value.items():
            print(f"Число {key_value} встречается {count_value} раз")

    @staticmethod
    def log_operation(operation_type, arguments, result_val, log_file_path):
        date_logging = datetime.now().date().strftime("%Y.%m.%d")
        time_logging = datetime.now().time().strftime("%H:%M:%S")

        log_entry = {
            "Операция": operation_type,
            "Аргументы": arguments,
            "Результат": result_val,
            "Дата": date_logging,
            "Время": time_logging
        }

        with open(log_file_path, "a", encoding="utf-8") as log_file_op:
            log_file_op.write(str(log_entry) + "\n")

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
            return 'Список пуст!'

    def calculate_result(self):
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

        try:
            for n in self.num_1:
                n.replace('.', '', 1)
                if n.isalpha() or n == '.':
                    self.num_1_invalid = True
                    raise ValueError

                if len(self.num_1) > 1 and ' ' in self.num_1:
                    self.num_1 = [int(n) for n in self.num_1]
                    self.flag_sp = True

                else:
                    self.num_1 = float(self.num_1)

        except ValueError:
            print(f'Некорректное значение "{self.num_1}"')

        try:
            if self.flag_sp is False:
                for n in self.num_2:
                    n.replace('.', '', 1)
                    if n.isalpha() or n == '.':
                        self.num_2_invalid = True
                        raise ValueError

                    else:
                        self.num_2 = float(self.num_2)

        except ValueError:
            print(f'Некорректное значение "{self.num_2}"')


if __name__ == "__main__":
    calc = NewCalc()

    factorial_cache = {}
    initialize_factorial_cache(factorial_cache)

    calc.input_info()
    calc.memo_plus(calc.calculate_result())
