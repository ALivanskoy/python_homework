# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

rnd = int(input("Введите количество знаков после запятой: "))
if rnd == 0:
    print("С учётом округления число π равно 3")
else:
    (f"С учётом округления число π равно {round(math.pi, rnd)}")