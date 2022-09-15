# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

from random import *

random_numbers = []
non_repeating_list = []

for i in range(randint(5, 10)):
    random_numbers.append(randint(1, 5))

print(f"Последовательность чисел: {random_numbers}")

non_repeating_list.append(random_numbers[0])
for i in random_numbers:
    if not i in non_repeating_list:
        non_repeating_list.append(i)

non_repeating_list.sort()

print(f"Cписок неповторяющихся элементов исходной последовательности: {non_repeating_list}")