# Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь
# my_dict, состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

my_dict = {'first_one': 'we can do it'}


def biggest_dict(**kwargs):
    my_dict.update(**kwargs)
    return my_dict


my_dict = biggest_dict(bad_joke="продам гараж", num=24, lost=(4, 8, 15, 16, 23, 42))

print(f"Полученный словарь: {my_dict}")