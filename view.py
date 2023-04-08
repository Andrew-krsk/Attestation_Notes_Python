import controller


def screen():
    action = ''
    action = input(
        "\n\nВыберете действие:\n1 - Создать заметку\n2 - Найти заметку"
        "\n3 - Просмотреть все заметки\n4 - Редактировать заметку\n5 - Удалить заметку\n6 - Выход из программы\nВведите "
        "цифру действия --> ")
    while (int(action) < 1 or int(action) > 6):
        action = input("ВЫБРАН НЕ ВЕРНЫЙ ПУНКТ !!!\nВведите верный пункт меню ")
    match action:
        case '1':
            controller.create_note()
        case '2':
            controller.find_note()
        case '3':
            controller.show_all_notes()
        case '4':
            controller.edit_note()
        case '5':
            controller.del_note()
        case '6':
            exit()
