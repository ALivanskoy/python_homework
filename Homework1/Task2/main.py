# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = [True, False]
Y = [True, False]
Z = [True, False]
check = True
for i in X:
    for j in Y:
        for k in Z:
            left = not (X[i] and Y[j] and Z[k])
            right = not X[i] or not Y[j] or not Z[k]
            print ("¬({} ⋁ {} ⋁ {}) = {}".format(X[i], Y[j], Z[k], left))
            print("¬{} ⋀ ¬{} ⋀ ¬{} = {}".format(X[i], Y[j], Z[k], right))
            print('\n')
            if left != right:
                check = False

print("Итоги проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат: {}".format(check))


