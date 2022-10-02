import csv_unit as cu
import os.path as op


def create_file():
    check = input(f"Введите имя файла или (d)efault, что бы оставить имя '{cu.defuault_name}'\n")
    fields = input(f"Введите поля файла через символ ';'или (d)efault, что бы оставить поля '{cu.defuault_fields}'\n")
    if check == "d":
        if fields == "d":
            cu.csv_creator(cu.defuault_name, cu.defuault_fields)
        else:
            fields = "id;" + fields
            fields.replace(" ", "")
            fields += "\n"
            cu.csv_creator(cu.defuault_name, fields)
    else: cu.csv_creator(check, fields)


def new_record():
    file = input(f"Введите имя файла или введите (d)efault, что бы оставить имя '{cu.defuault_name}'  \n")
    fields = ""
    if file == "d":
        file = cu.defuault_name
    data = cu.csv_head_reader(file)
    for i in range(len(data)+1):
        fields += input(f"\n{data[i]} = ") + ";"
        print(fields)
    fields += "\n"
    print(fields)
    cu.csv_writer(file, fields)
    print(f'В файл "{file}" добавлена запись')


def base_reader():
    check = input(f"Введите имя файла для чтения или введите (d)efault, что бы оставить имя '{cu.defuault_name}'\n")
    data = None
    if check == "d":
        data = cu.csv_reader(cu.defuault_name)
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
        line = ''
        length = 70
        print("-"*length)
        for i in base:
            for j in i:
                line += j + "\t\t"
            print(line)
            line = ""
            print("-"*length)
