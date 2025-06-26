import time
from basic_calc import BasicCalc


class ExecutionTimer:
    def __enter__(self):
        self.start_time = time.time()
        return self.start_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        duration = time.time() - self.start_time
        print(f" Время выполнения операции: {duration:.4f} секунд")


factorial_cache = {}


def cache_result(func):

    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key in factorial_cache:
            print("  -> Результат взят из кэша")
            return factorial_cache[key]
        else:
            print("  -> Вычисляем результат...")
            calculated_result = func(*args, **kwargs)
            factorial_cache[key] = calculated_result
            return calculated_result
    return wrapper


@cache_result
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def initialize_factorial_cache(limit=100):
    for i in range(limit + 1):
        yield f"Факториал {i} посчитан и добавлен в кэш. Результат: {factorial_recursive(i)}"


class NewCalc(BasicCalc):
    def __init__(self):
        super().__init__()
        self.memory = []

    @staticmethod
    def log_operation(operation_type, arguments, result_val):
        # Логирование операции
        log_entry = {
            "Операция": operation_type,
            "Аргументы": arguments,
            "Результат": result_val
        }
        # Записываем логи в файл
        with open("calculator_log.txt", "a", encoding="utf-8") as log_file_op:
            log_file_op.write(str(log_entry) + "\n")

    def memo_plus(self, number=None):
        if len(self.memory) < 3:
            self.memory.append(number)
            self.log_operation("memo_plus", [number], None)
        else:
            raise MemoryError("Все ячейки памяти заполнены!")

    def memo_minus(self):
        if self.memory:
            removed = self.memory.pop()
            self.log_operation("memo_minus", [removed], None)
            print(f'Удалено значение: {removed}')
            return removed
        else:
            raise MemoryError("Значений в памяти нет!")

    @property
    def top_memory(self):
        if len(self.memory) > 0:
            top_value = self.memory[-1]
            self.log_operation("top_memory", [], top_value)
            return top_value
        else:
            raise MemoryError("Список пуст!")

    def check_and_calculate_result(self):
        calculated_result = super().check_and_calculate_result()
        if calculated_result is not None:
            self.log_operation("выражение", (self.num_1, self.num_2), calculated_result)
        return calculated_result


if __name__ == "__main__":
    for _ in initialize_factorial_cache(limit=10):
        pass
    print("Инициализация кэша завершена.")

    calc = NewCalc()
    calc.input_info()

    try:
        result = calc.check_and_calculate_result()
    except MemoryError as e:
        print(f"Ошибка при работе с памятью: {e}")
    except ValueError as e:
        print(f"Ошибка ввода или вычисления: {e}")
