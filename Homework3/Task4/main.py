# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal_number = int(input("Введите десятичное число: "))
bin_number = ""


if decimal_number > 0:
    while decimal_number > 0:
        bin_number = str(decimal_number % 2) + bin_number
        decimal_number = int(decimal_number / 2)
elif decimal_number == 0:
    bin_number = "0"
else:
    decimal_number = abs(decimal_number)
    while decimal_number > 0:
        bin_number = str(decimal_number % 2) + bin_number
        decimal_number = int(decimal_number / 2)
    bin_number = "-" + bin_number

print("Тут могла бы быть Ваша реклама")
print(f"Получилось двоичное число: {bin_number}")