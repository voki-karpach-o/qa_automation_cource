import re


def calc_multiply(first, second):
    s = first * second
    print(s)


def calc_divide(first, second):
    s = first / second
    print(s)


def calc_subtract(first, second):
    s = first - second
    print(s)


def calc_add(first, second=None):
    if second is None:
        print(sum(first))
    else:
        print(first + second)


operations = {
    '+': calc_add,
    '-': calc_subtract,
    '*': calc_multiply,
    '/': calc_divide
}

pattern = r'^(\d+(\.\d+)?)([+\-*/])(\d+(\.\d+)?)$'
flag_expression = False
flag_letters = False
flag_dot = False
flag_sp = False

# объявление переменных чтобы не ругался на отсутсвие operation и num_2 в 90 строке
operation = None
num_2 = None

# ввод и проверка введенных данных
while True:
    num_1 = input('Введи цифру или математическое выражение без пробелов: ')
    match = re.fullmatch(pattern, num_1)

    # проверка на ввод выражения в строку
    if match:
        first_num, _, operation, second_num, _ = match.groups()
        first_num = float(first_num) if '.' in first_num else int(first_num)
        second_num = float(second_num) if '.' in second_num else int(second_num)
        operations[operation](first_num, second_num)
        flag_expression = True
        break
    else:
        # проверка на наличие букв
        for n in num_1:
            n.replace('.', '', 1)
            if n.isalpha():
                flag_letters = True
                break
            elif n == '.':
                flag_dot = True
                break
        if flag_letters is True or flag_dot is True:
            print('Недопустимая операция!')
            flag_letters = False
            flag_dot = False
            continue
        else:
            if len(num_1) > 1 and ' ' in num_1:
                num_1 = [int(n) for n in num_1.split()]
                flag_sp = True
                break
            elif '.' in num_1:
                num_1 = float(num_1)
                break
            elif '.' not in num_1:
                num_1 = int(num_1)
                break

# если в строку ввода ввели не выражение а число
if flag_expression is False:
    while True:
        operation = input('Выберите знак математической операции: +, -, *, /  ')
        if operation not in operations:
            print('Недопустимая операция!')
            continue
        else:
            break

    if flag_sp is False:
        while True:
            num_2 = input('Введи цифру: ')

            # проверка на наличие букв
            for n in num_2:
                n.replace('.', '', 1)
                if n.isalpha():
                    flag_letters = True
                    break
                elif n == '.':
                    flag_dot = True
                    break
            if flag_letters is True or flag_dot is True:
                print('Недопустимая операция!')
                flag_letters = False
                flag_dot = False
                continue
            else:
                if '.' in num_2:
                    num_2 = float(num_2)
                    break
                elif '.' not in num_2:
                    num_2 = int(num_2)
                    break

# вызов функции, если в строку ввода ввели не выражение а число
if flag_expression is False:
    if flag_sp:
        operations[operation](num_1)
    else:
        operations[operation](num_1, num_2)
