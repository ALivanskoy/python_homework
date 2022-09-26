import csv_unit as cu
import os.path as op
import random as r


def new_base():
    check = input("Создать новый файл?\n (y)es / (n)o\n")
    if check == "y":
        check = input("Введите имя файла или введите (d)efault, что бы оставить имя по-умолчанию\n")
        if check == "d":
            cu.csv_creator()
        else: cu.csv_creator(check)


def new_record():
    file = input("Введите имя файла или введите (d)efault, что бы оставить имя по-умолчанию  \n")
    if file == "d":
        file = 'phone base'

    name = input("Введите имя Абонента или введите (d)efault, что бы оставить имя по-умолчанию  \n")
    if name == "d":
        name = 'defaul_Name'

    phone = input("Введите номер Абонента или введите (d)efault, что бы в номер записалось хоть что-то  \n")
    if phone == "d":
        phone = r.randint(10**6, 10**7)
    id = r.randint(0, 100000)

    cu.csv_writer(file, id, name, phone)
    print(f'В файл "{file}" добавлена запись:\nid = {id}, Имя = {name}, Номер = {phone}\n')


def base_reader(file_name="phone base"):
    check = input("Введите имя файла для чтения или введите (d)efault, что бы оставить имя по-умолчанию\n")
    data = None
    if check == "d":
        data = cu.csv_reader(file_name)
        data = data.split("\n")
        string_base = [rows.split(";") for rows in data]
        return string_base

    elif op.exists(check):
        data = cu.csv_reader(check)
        data = data.split("\n")
        string_base = [rows.split(";") for rows in data]
        return string_base
    else:
        string_base = [-1, check]
        return string_base


def show_base(base):

    if base[0] == -1:
        print(f"Ошибка чтения базы\nФайл '{base[1]}' не найден\n")
    else:
        length = 70
        print("-"*length+"\n")
        for i in base:
            print(f"\t{i[0]}\t{i[1]}\t\t{i[2]}\n")
            print("-"*length)
        print(f"\n{'*'*19} Тут могла бы быть ваша реклама {'*'*19}\n")
