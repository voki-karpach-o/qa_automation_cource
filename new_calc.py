import re
import time
import math
import collections
import random
from datetime import datetime
from basic_calc import BasicCalc


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
    memory = []

    def generate_random_numbers(self):
        pass

    def log_operation(self, operation_type, arguments, result_val):
        date_logging = datetime.now().date().strftime("%Y.%m.%d")
        time_logging = datetime.now().time().strftime("%H:%M:%S")

        log_entry = {
            "Операция": operation_type,
            "Аргументы": arguments,
            "Результат": result_val,
            "Дата": date_logging,
            "Время": time_logging
        }
        with open("calculator_log.txt", "a", encoding="utf-8") as log_file_op:
            log_file_op.write(str(log_entry) + "\n")

    @staticmethod
    def memo_plus(number=None):
        try:
            if len(NewCalc.memory) < 3:
                NewCalc.memory.append(number)
                print(f'Добавлено значение: {number}')
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

        while True:
            for ch in self.num_1:
                ch.replace('.', '', 1)
                if ch.isalpha() or ch == '.':
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
                for ch in self.num_2:
                    ch.replace('.', '', 1)
                    if ch.isalpha() or ch == '.':
                        print(f'Некорректное значение "{self.num_2}", заменено на 0')
                        self.num_2 = '0'
                        break

                self.num_2 = float(self.num_2)
                break


if __name__ == "__main__":
    calc = NewCalc()

    factorial_cache = {}
    initialize_factorial_cache(factorial_cache)

    while True:
        start_off_value_input = input(
            'Введи "Начать" или "Продолжить" чтобы начать или продолжить, "Факториал" чтобы вычислить, '
            '"Выйти" чтобы выйти, "Значение", "Удалить" чтобы удалить последнее значение: ').strip().upper()

        if start_off_value_input in ('ПРОДОЛЖИТЬ', 'НАЧАТЬ'):
            with ExecutionTimer():
                calc.set_info()
                result = calc.check_input()

                if result is not None:
                    calc.memo_plus(result)
                else:
                    result = calc.calculate_result()
                    calc.log_operation(calc.operation, (calc.num_1, calc.num_2), result)
                    calc.memo_plus(result)

        elif start_off_value_input == 'ФАКТОРИАЛ':
            value = input('Введи "Обычный", если нужен обычный факториал или "Рекурсивный", если нужен рекурсивный ').upper()
            if value == 'РЕКУРСИВНЫЙ':
                try:
                    num = int(input("Введите число для вычисления факториала: "))
                    with ExecutionTimer():
                        result_fact = factorial_recursive(num)
                    print(f"Факториал {num} = {result_fact}")
                except Exception as e:
                    print(f"Ошибка: {e}")
            elif value == 'ОБЫЧНЫЙ':
                try:
                    num = int(input("Введите число для вычисления факториала: "))
                    with ExecutionTimer():
                        result_fact = factorial_regular(num)
                    print(f"Факториал {num} = {result_fact}")
                except Exception as e:
                    print(f"Ошибка: {e}")

        elif start_off_value_input == 'УДАЛИТЬ':
            calc.memo_minus()

        elif start_off_value_input == 'ВЫЙТИ':
            break

        elif start_off_value_input == 'ЗНАЧЕНИЕ':
            print(calc.top_memory)

        else:
            print('Введите только "Продолжить", "Удалить", "Факториал", "Выйти" или "Значение"!')
