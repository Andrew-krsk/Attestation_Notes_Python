import os
import datetime

import view


def create_note():
    today = datetime.datetime.today()
    today = today.strftime("%m/%d/%Y")
    name = input('Введите название заметки и нажмите "Enter"\n')
    text = input('Напишите техт заметки и нажмите "Enter"\n')
    if os.path.exists('notes.csv'):
        db = read_db()
        id = len(db) + 1
    else:
        with open("notes.csv", "w", encoding='utf-8') as file:
            id = 1
    note = f"{id}; {name}; {text}; {today}"
    with open("notes.csv", "a", encoding='utf-8') as file:
        file.write(f'{note}\n')
    file.close()
    print(f"\nЗаметка сохранена под номером {id}")
    view.screen()


def read_db():
    notes = []
    with open("notes.csv", "r", encoding='utf-8') as file:
        temp = []
        while True:
            temp_note = {}
            val = []
            line = file.readline().replace("\n", "")
            if line != "":
                temp = line.split(";")
            else:
                break
            val.append(temp[1])
            val.append(temp[2])
            val.append(temp[3])
            temp_note[temp[0]] = val
            notes.append(temp_note)
        file.close()
    return notes


def print_note(note):
    result = []
    for keys, val in note.items():
        result.append(val[0])
        result.append(val[1])
        result.append(val[2])
        if len(val) > 3:
            result.append(val[3])
    if len(result) == 0:
        print("\nЗаметки с таким номер не существует")
    else:
        print(f"\nЗаметка №{keys}\nНазвание:{result[0]}\nТекст:{result[1]}\nДата создания:{result[2]}")
    if len(note.values()) == 4:
        print(f"Дата последнего изменения: {result[3]}")


def find_note():
    action = input(
        "\nВыберете метод поиска:\n1 - по номеру:\n2 - по названию:\n3 - по содержимому:"
        "\n4 - по дате:\n5 - выход в главное меню:\n6 - Выход из программы\nВведите цифру действия --> ")
    while (int(action) < 1 or int(action) > 6):
        action = input("ВЫБРАН НЕ ВЕРНЫЙ ПУНКТ !!!\nВведите верный пункт меню ")
    match action:
        case '1':
            action = input("Введите номер заметки -->")
            db = read_db()
            for item in db:
                for key, val in item.items():
                    if action == key:
                        print_note(item)
            view.screen()
        case '2':
            action = input("Введите название заметки -->")
            db = read_db()
            for item in db:
                for key, val in item.items():
                    if action in val[0]:
                        print_note(item)
            view.screen()
        case '3':
            action = input("Введите содержимое заметки -->")
            db = read_db()
            for item in db:
                for key, val in item.items():
                    if action in val[1]:
                        print_note(item)
            view.screen()
        case '4':
            action = input("Введите число, месяц или год создания заметки -->")
            db = read_db()
            for item in db:
                for key, val in item.items():
                    if action in val[2]:
                        print_note(item)
            view.screen()
        case '5':
            view.screen()
        case '6':
            exit()


def show_all_notes():
    db = read_db()
    for item in db:
        result = []
        for keys, val in item.items():
            result.append(val[0])
            result.append(val[1])
            result.append(val[2])
            if len(val) > 3:
                result.append(val[3])
            if len(result) == 0:
                print("Заметок нет")
            else:
                print(f"\nЗаметка №{keys}\nНазвание:{result[0]}\nТекст:{result[1]}\nДата создания:{result[2]}")
            if len(item.values()) == 4:
                print(f"Дата последнего изменения:{result[3]}")
    view.screen()


def edit_note():
    numb = input("\nВведите номер заметки, которую необходимо отредактировать:\n--> ")
    db = read_db()
    edit = {}
    for item in db:
        for key, val in item.items():
            if numb == key:
                edit = item
    for i in range(len(db) - 1):
        for key, val in db[i].items():
            if numb == key:
                db.remove(db[i])
    action = input(
        "\nВыберете пункт редактирования:\n1 - редактировть название заметки:\n2 - редактировть текст заметки:\nВведите пункт --> ")
    while (int(action) < 1 or int(action) > 2):
        action = input("ВЫБРАН НЕ ВЕРНЫЙ ПУНКТ !!!\nВведите верный пункт меню ")
    today = datetime.datetime.today()
    today = today.strftime("%m/%d/%Y")
    print_note(edit)
    match action:
        case '1':
            result = []
            for keys, val in edit.items():
                result.append(val[1])
                result.append(val[2])
            action = input("\nВведите новое название заметки --> ")
            new_note = {}
            new_note[numb] = [action, result[0], result[1], today]
            db.append(new_note)
            with open("notes.csv", "w", encoding='utf-8') as file:
                for i in range(len(db)):
                    item = str(db[i]).replace("{", "").replace("}", "").replace("'", "").replace(":", ",") \
                        .replace("[", "").replace("]", "").replace(",", ";")
                    file.write(f'{item}\n')
                file.close()
            print("Запись сохранена")
            view.screen()
        case '2':
            result = []
            for keys, val in edit.items():
                result.append(val[0])
                result.append(val[2])
            action = input("\nВведите новый текст заметки --> ")
            new_note = {}
            new_note[numb] = [result[0], action, result[1], today]
            db.append(new_note)
            with open("notes.csv", "w", encoding='utf-8') as file:
                for i in range(len(db)):
                    item = str(db[i]).replace("{", "").replace("}", "").replace("'", "").replace(":", ",") \
                        .replace("[", "").replace("]", "").replace(",", ";")
                    file.write(f'{item}\n')
                file.close()
            print("Запись сохранена\n")
            view.screen()


def del_note():
    numb = input("Введите номер заметки, которую необходимо удалить --> ")
    db = read_db()
    for i in range(len(db)-1):
        for key, val in db[i].items():
            if numb == key:
                db.remove(db[i])
    with open("notes.csv", "w", encoding='utf-8') as file:
        for i in range(len(db)):
            item = str(db[i]).replace("{", "").replace("}", "").replace("'", "").replace(":", ",") \
                .replace("[", "").replace("]", "").replace(",", ";")
            file.write(f'{item}\n')
        file.close()
    print("Запись удалена\n")
    view.screen()
