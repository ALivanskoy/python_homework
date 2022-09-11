# 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# 2. Реализуйте алгоритм перемешивания списка.

import random

number = int(input("Введите число: "))
list = []

for i in range(number):
    list.append(random.randint(-number, number))

print(f"Список рандомных чисел: {list}")

with open("file.txt", "r") as data:
    indexes = data.read().splitlines()
    print(f"Список индексов в файле file.txt: {indexes}")
    for i in indexes:
            i = int(i)
            if (i <= number and i > 0):
                print(f"В приведённом списке на позиции {i} число {list[i-1]}")
            else: print(f"В приведённом списке нет элемента с индексом {i}")

random.shuffle(list)
print(f"Перемешанный список рандомных чисел: {list}")

