# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

list = []
mux_list = []


for i in range(random.randint(3, 6)):
    list.append(random.randint(1, 9))

print(f"Список из нескольких чисел: {list}")

if int(len(list)) % 2 == 0:
    for i in range (0, int(len(list)/2)):
        mux = list[i] * list[-i-1]
        mux_list.append(mux)
else:
    for i in range (0, int(len(list)/2 + 1)):
        mux = list[i] * list[-i-1]
        mux_list.append(mux)

print(f"Список из произведений пары чисел: {mux_list}")

mux = 1
for i in range (0, int(len(mux_list) - 1)):
    mux *= mux_list[i]
print(f"Произведение пар чисел списка: {mux}")