# Задача 41: Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Добавьте возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

import re


def get_expression_list(somestr):
    # Метод получает строку somestr с математическим выражением и преобразовывает её в список чисел и символов
    expression_numbers = re.findall(r'\d*\.\d+|\d+', somestr)
    expression_sign = [i for i in somestr if i in "+-/*"]
    expression_list = []
    for i in range(len(expression_numbers)):
        if i < len(expression_sign):
            expression_list.append(expression_numbers[i])
            expression_list.append(expression_sign[i])
        else:
            expression_list.append(expression_numbers[i])
    return expression_list


def basic_calculation (somelist):
    # Метод получает список somelist с математическим выражением и выполняет математические операции " +,-,/,* "
    # приоритет операций стандартный

    # В методе используется цикл while, a не for, т.к. длина списка в теле цикла постоянно уменьшается
    i = 0
    while "*" in somelist:
        if somelist[i] == "*":
            somelist[i - 1] = float(somelist[i - 1]) * float(somelist[i + 1])
            somelist.pop(i + 1)
            somelist.pop(i)
            i = 0
        i += 1

    i = 0
    while "/" in somelist:
        if somelist[i] == "/":
            somelist[i - 1] = float(somelist[i - 1]) / float(somelist[i + 1])
            somelist.pop(i + 1)
            somelist.pop(i)
            i = 0
        i += 1

    i = 0
    while "-" in somelist:
        if somelist[i] == "-":
            somelist[i - 1] = float(somelist[i - 1]) - float(somelist[i + 1])
            somelist.pop(i + 1)
            somelist.pop(i)
            i = 0
        i += 1

    i = 0
    while "+" in somelist:
        if somelist[i] == "+":
            somelist[i - 1] = float(somelist[i - 1]) + float(somelist[i + 1])
            somelist.pop(i + 1)
            somelist.pop(i)
            i = 0
        i += 1
    return somelist[0]


def in_brackets (somestr):
    out_str = somestr[somestr.index('(') + 1 : somestr.index(')') ]
    return out_str


def myeval(somelist):

    while "(" in somelist: #заменяем все скобки на эквивалент их значений
        brackets = in_brackets(somelist)
        calculations = str(basic_calculation(get_expression_list(brackets)))
        somelist = somelist.replace(f"({brackets})", calculations, 1)
    expression = basic_calculation(get_expression_list(somelist))
    return expression


expression = '123+45*6/4-(8+91)/5'

print(f"\n{'-'*50}\nВыражение для подсчёта: {expression}")
print(f"{'-'*50}\nРезультат работы самопальной eval: {myeval(expression)}")
print(f"{'-'*50}\nРезультат работы питоновской eval: {eval(expression)}\n{'-'*50}\n")