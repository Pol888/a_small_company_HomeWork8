import menu
import search_selection
import read_and_write_in_database
import database_operations
import exporting_data


def connecting_function():
    file = read_and_write_in_database.read_json()
    while True:
        button_number = menu.show_menu()
        if button_number == 1:
            search_selection.search_name(file)
        elif button_number == 2 or button_number == 3:
            search_selection.selection(file, button_number)
        elif button_number == 4:
            file = database_operations.add_an_employee(file)
        elif button_number == 5:
            file = database_operations.deleting_an_employee(file)
        elif button_number == 6:
            file = database_operations.changing_data(file)
        elif button_number == 7:
            exporting_data.write_json2(file)
        elif button_number == 8:
            exporting_data.write_csv2(file)
        elif button_number == 9:
            save = input("Сохранить изменения? 1. - да, выйти, 2. - нет, выйти без сохранения.\n")
            if save == '1':
                print('Идет сохранение в базу данных..')
                read_and_write_in_database.write_json(file)
            break











