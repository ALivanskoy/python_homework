# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


number = int(input("Задайте натуральное число: "))
simple_multipliers = []

for i in range(1, abs(number) + 1):
    if abs(number) % i == 0:
        simple_multipliers.append(i)

print(f"Список простых множителей числа {number}:\n{simple_multipliers}")