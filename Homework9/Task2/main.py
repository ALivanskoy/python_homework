# Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка
# будут соответствовать правилам задания ключей в словарях.

def to_dict(lst):
    dict = {}
    for i in lst:
        dict [i] = i
    return dict


list_one = ["продам гараж", 24, (4, 8, 15, 16, 23, 42)]
print(f"Исходных список:\n {list_one}")
print(f"Словарь:\n {to_dict(list_one)}")