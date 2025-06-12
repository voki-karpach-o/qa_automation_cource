from basic_calc import BasicCalc
import re


class NewCalc(BasicCalc):
    memory = []

    @staticmethod
    def log_operation(operation_type, arguments, result_val):
        log_entry = {
            "Операция": operation_type,
            "Аргументы": arguments,
            "Результат": result_val
        }
        with open("calculator_log.txt", "a", encoding="utf-8") as log_file_op:
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

        else:
            try:
                self.num_1 = float(self.num_1)
            except ValueError:
                print(f"Невалидное значение для первого числа ('{self.num_1}')! Заменено на 0.")
                self.num_1 = 0

            try:
                self.num_2 = float(self.num_2)
            except ValueError:
                print(f"Невалидное значение для второго числа ('{self.num_2}')! Заменено на 0.")
                self.num_2 = 0

        if self.flag_expression is False:
            if self.flag_sp:
                calculated_result = self.operations[self.operation](self.num_1)
            else:
                calculated_result = self.operations[self.operation](self.num_1, self.num_2)

            print(calculated_result)
            self.last_result = calculated_result
            return calculated_result


if __name__ == "__main__":
    calc = NewCalc()
    calc.input_info()

    try:
        result = calc.check_and_calculate_result()
    except MemoryError as m:
        print(f"Произошла непредвиденная ошибка: {m}")
    except ValueError as v:
        print(f"Произошла непредвиденная ошибка: {v}")
    except IndexError as i:
        print(f"Произошла непредвиденная ошибка: {i}")
