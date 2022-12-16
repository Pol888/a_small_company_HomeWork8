def search_name(file):
    x = int(input('По какому критерию осуществлять поиск?  1. - id,  2. - Имя и Фамилия\n'))
    if x == 1:
        id_I = int(input('Введите id сотрудника\n'))
        for i in file:
            if i['id'] == id_I:
                print(f'ID Сотрудника - {id_I}, Имя - {i["last_name"]}, Фамилия - {i["first_name"]},'
                      f' Должность - {i["position"]}, Номер для связи - {i["phone_number"]}, Заработная плата = {i["salary"]}.')

    elif x == 2:
        name = input('Введите имя сотрудника или пропустите ввод нажатием Enter\n')
        surname = input('Введите фамилию сотрудника или пропустите ввод нажатием Enter\n')
        for i in file:
            if len(name) > 0 and len(surname) > 0:
                if name.lower() == i["last_name"].lower() and surname.lower() == i["first_name"].lower():
                    print(f'ID Сотрудника - {i["id"]}, Имя - {i["last_name"]}, Фамилия - {i["first_name"]},'
                          f' Должность - {i["position"]}, Номер для связи - {i["phone_number"]}, Заработная плата = {i["salary"]}.')

            elif (len(name) > 0 and len(surname) == 0) or (len(name) == 0 and len(surname) > 0):
                if name.lower() == i["last_name"].lower() or surname.lower() == i["first_name"].lower():
                    print(f'ID Сотрудника - {i["id"]}, Имя - {i["last_name"]}, Фамилия - {i["first_name"]},'
                          f' Должность - {i["position"]}, Номер для связи - {i["phone_number"]}, Заработная плата = {i["salary"]}.')


def selection(file, num):
    a = set()
    for i in file:
        a.add(i["position"])

    if num == 2:
        print(f'В базе имеются следующие наименования должностей...{a}')
        position = input('Введите должность для поиска\n')
        for i in file:
            if i["position"].lower() == position.lower():
                print(f'ID Сотрудника - {i["id"]}, Имя - {i["last_name"]}, Фамилия - {i["first_name"]},'
                      f' Должность - {i["position"]}, Номер для связи - {i["phone_number"]}, Заработная плата = {i["salary"]}.')

    elif num == 3:
        start = float(input('От какой суммы вести поиск? Формат ввода - (77000.00) - (рубли.копейки)\n'))
        end = float(input('До какой суммы вести поиск? Формат ввода - (77000.00) - (рубли.копейки)\n'))
        for i in file:
            if start <= i["salary"] <= end:
                print(f'ID Сотрудника - {i["id"]}, Имя - {i["last_name"]}, Фамилия - {i["first_name"]},'
                      f' Должность - {i["position"]}, Номер для связи - {i["phone_number"]}, Заработная плата = {i["salary"]}.')