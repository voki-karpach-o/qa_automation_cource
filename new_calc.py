from basic_calc import BasicCalc


class NewCalc(BasicCalc):
    memory = []

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
    calc = NewCalc()
    calc.input_info()

    try:
        result = calc.check_and_calculate_result()
    except (MemoryError, ValueError, IndexError) as e:
        print(f"Произошла ошибка: {e}")
