def csv_creator(file_name = "phone base"):
    print(f"Создание файла {file_name}.csv\n")
    with open(f'{file_name}.csv', 'w', newline='') as csvfile:
        csvfile.write(f"id; Имя; Номер\n")
        print(f"Файл {file_name}.csv создан\n")


def csv_reader(file_name):
    with open(f'{file_name}.csv', 'r') as csvfile:
        data = csvfile.read()
        return data

def csv_writer(file_name, id, name, phone):
    with open(f'{file_name}.csv', 'a', newline='') as csvfile:
        csvfile.writelines(f"{id}; {name}; {phone}")


