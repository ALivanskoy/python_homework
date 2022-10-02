defuault_name = "base"
defuault_fields = "id; Name; Phone"

def csv_creator(file_name, fields):
    print(f"Создание файла {file_name}.csv\n")
    with open(f'{file_name}.csv', 'w') as csvfile:
        csvfile.write(f"{fields}\n")
        print(f"Файл {file_name}.csv создан\n")


def csv_reader(file_name):
    with open(f'{file_name}.csv', 'r') as csvfile:
        data = csvfile.read()
        return data

def csv_reader(file_name):
    with open(f'{file_name}.csv', 'r') as csvfile:
        data = csvfile.read()
        return data


def csv_head_reader(file_name):
    with open(f'{file_name}.csv', 'r') as csvfile:
        data = csvfile.readline().replace(" ", "").replace("\n", "").split(";")
        return data


def csv_writer(file_name, fields):
    with open(f'{file_name}.csv', 'a') as csvfile:
        csvfile.writelines(fields)
