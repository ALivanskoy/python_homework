# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def getcoefficient(input_string): #Метод делит строку на набор коэффициентов вида коэффициент:степень
    input_string = input_string.replace(' ', '').replace('=0', '').replace('*x^', ':').split('+')
    if input_string[-1].isdigit():
        input_string[-1] = input_string[-1] + ':0' # Добавляем к последнему элементу степень нуля
    return input_string


with open("poly1.txt", 'r') as data:
    poly1 = data.read() #Получаем строку первого многочлена
with open("poly2.txt", 'r') as data:
    poly2 = data.read() #Получаем строку второго многочлена

poly3 = ""

print(poly1)
print(poly2)

poly1_coefficient = getcoefficient(poly1) # Преобразовываем к списку вида -
poly2_coefficient = getcoefficient(poly2) # коэффициент:степень
print(poly1_coefficient)

for i in poly1_coefficient:
    index_one = i.split(':')
    for j in poly2_coefficient:
        index_two = j.split(':')
        if index_one[1] == index_two[1]:
            poly3 += str(int(index_one[0])+int(index_two[0])) + "x" + index_one[1] + " + "
            break
        elif int(index_one[1]) > int (index_two[1]):
            poly3 += str(index_one[0]) + "x" + index_one[1] + " + "
            non_repeat = False
        elif int(index_one[1]) < int (index_two[1]):
            poly3 += str(index_two[0]) + "x" + index_one[1]+ " + "
            non_repeat = False

        print(poly3)