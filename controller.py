import view
import module
import datetime

def start():
    while True:
        view.menu_console()
        user_input = input()
        if user_input == '1':
            module.show("all")
        elif user_input == '2':
            module.show("ID")
        elif user_input == '3':
            module.show("date")
        elif user_input == '4':
            module.show("all")
            module.change_note()
        elif user_input == '5':
            module.add_note()
        elif user_input == '6':
            module.show("all")
            module.del_notes()
        else:
            print("Программа Журнал заметок завершена")
            break

