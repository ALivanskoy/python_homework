# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


numbers = [1, 2, 3, 5, 1, 5, 3, 10]
print(f"Исходная последовательность: {numbers}")

numbers = list(set(numbers))

print(f"Cписок уникальных элементов заданной последовательности: {numbers}")