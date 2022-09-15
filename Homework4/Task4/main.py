# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import *

def Polynomial ():
    polynomial = ""
    for i in range(degree, -1, -1):
        coefficient = str(randint(0, 100))
        if i > 0 and coefficient != '0':
            polynomial += coefficient + "*x^" + str(i) + " + "
        elif i == 0 and coefficient != '0':
            polynomial += coefficient
    polynomial += " = 0"
    return polynomial

poly = []
degree = int(input("Задайте натуральную степень: "))
if degree <= 0 or degree > 5:
    print("Это просто учебная задача, не переусложняй")
else:
    poly = Polynomial()
    print (f"Получился многочлен: {poly}")


with open("file.txt", "w") as data:
    data.write(poly)
    print('Многочлен записан в файл "file.txt"')