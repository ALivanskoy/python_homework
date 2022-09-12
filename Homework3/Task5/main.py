# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input("Задайте число: "))
fibonacci = []
full_fibonacci = []

for i in range(0, number):
    if i == 0:
        fibonacci.append(0)
    elif i == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[i-2] + fibonacci[i-1])

for i in range(1, int(len(fibonacci)*2)):
    if i <= int(len(fibonacci)):
        full_fibonacci.append(-fibonacci[-i])
    else:
        full_fibonacci.append(fibonacci[i - int(len(fibonacci))])


print(f"Cписок чисел Фибоначчи:\n{full_fibonacci}")


