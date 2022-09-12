# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

list = []

for i in range(random.randint(3, 6)):
    list.append (round(float(random.randint(1, 9)) + float(random.randint(0, 99) * 0.01), 2))

print(f"Список из вещественных чисел: {list}")

max_float_part = list[0] % 1
min_float_part = list[0] % 1

for i in range (0, int(len(list))):
    if max_float_part < list[i] % 1:
        max_float_part = list[i] % 1
    elif min_float_part > list[i] % 1:
        min_float_part = list[i] % 1

print(f"Разница между максимальным и минимальным значением дробной части элементов списка: {round(max_float_part - min_float_part, 2)}")
