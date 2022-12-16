def add_an_employee(file):
    file1 = file
    print('Процесс добавления сотрудника..')
    dict_employee = {}
    dict_employee["id"] = file[-1]['id'] + 1
    dict_employee["last_name"] = input('Введите имя\n')
    dict_employee["first_name"] = input('Введите фамилию\n')
    dict_employee["position"] = input('Введите должность\n')
    dict_employee["phone_number"] = input('Введите номер телефона\n')
    dict_employee["salary"] = float(input('Введите заработную плату\n'))
    print(dict_employee)
    print('Внесение будет сохранено после завершения работы программы')
    print(dict_employee)
    file1.append(dict_employee)
    return file1


def deleting_an_employee(file):
    file1 = file
    print('Процесс удаления сотрудника..')
    x = int(input('По какому критерию осуществлять удаление?  1. - id,  2. - Имя и Фамилия\n'))
    if x == 1:
        id_del = int(input('Введите id\n'))
        for i in file1:
            if id_del == i['id']:
                print('Сотрудник найден')
                print(i)
                deL = int(input('Хотите удалить сотрудника 1. - да, 2. - нет\n'))
                if deL == 1:
                    del file1[i['id'] - 1]
                    print('В связи с удалением сотрудника id некоторых сотрудников может измениться')
                    for j in range(len(file1)):
                        file1[j]['id'] = j + 1
    elif x == 2:
        name = input('Введите имя сотрудника или пропустите ввод нажатием Enter\n')
        surname = input('Введите фамилию сотрудника или пропустите ввод нажатием Enter\n')
        for num, i in enumerate(file1):
            if name.lower() == i["last_name"].lower() and surname.lower() == i["first_name"].lower():
                print(f'{num + 1}. Сотрудник найден')
                print(i)
                b = int(input('Удалить данного сотрудника? 1. - да, 2. - нет\n'))
                if b == 1:
                    del file1[num]
        print('В связи с удалением сотрудника id некоторых сотрудников может измениться')
        for j in range(len(file1)):
            file1[j]['id'] = j + 1

    return file1


def changing_data(file):
    file1 = file
    print('Процесс внесения изменений в карточку сотрудника..')
    x = int(input('По какому критерию осуществлять поиск сотрудника?  1. - id,  2. - Имя и Фамилия\n'))
    if x == 1:
        id_ch = int(input('Введите id\n'))
        for i in range(len(file1)):
            if id_ch == file1[i]['id']:
                while True:
                    print('Сотрудник найден')
                    print(file1[i])
                    print('Какую колонку вы хотите изменить?')
                    print('ВАРИАНТЫ: last_name, first_name, position, phone_number, salary')
                    d = input('введите название колонки\n')
                    file1[i][d] = input('Введите новые данные\n')
                    print(file1[i])
                    z = input('Продолжить ? 1. да,  2. - нет\n')
                    if z == '2':
                        break
    elif x == 2:
        name = input('Введите имя сотрудника или пропустите ввод нажатием Enter\n')
        surname = input('Введите фамилию сотрудника или пропустите ввод нажатием Enter\n')
        for num, i in enumerate(file1):
            if name.lower() == i["last_name"].lower() and surname.lower() == i["first_name"].lower():
                print('Сотрудник найден')
                print(file1[num])
                print('Какую колонку вы хотите изменить?')
                print('ВАРИАНТЫ: last_name, first_name, position, phone_number, salary')
                d = input('введите название колонки\n')
                file1[num][d] = input('Введите новые данные\n')
                print(file1[num])
                z = input('Продолжить ? 1. да,  2. - нет\n')
                if z == '2':
                    break
    return file1
