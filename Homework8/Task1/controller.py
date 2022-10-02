import logic as l

def press_f_to_pay_respect():
    arg = None

    while arg != "0":
        print("Список доступных действий:\n")
        print("(1) Создать базу\n")
        print("(2) Добавить запись\n")
        print("(3) Отобразить базу\n")
        print("(0) Выйти\n")
        print("Ожидается ввод числа без кавычек\n")
        arg = input("Введите ваш вариант: \n")
        if arg == "1":
            l.create_file()
        elif arg == "2":
            l.new_record()
        elif arg == "3":
            l.show_base(l.base_reader())
        elif arg == "0":
            print("Приходите к нам ещё")
            break
        else:
            print("Неверный ввод. Попробуйте ещё раз\n\n\n")