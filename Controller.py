import os
import datetime


def Create_note():
    today = datetime.datetime.today()
    today = today.strftime("%m/%d/%Y")
    name = input('Введите название заметки и нажмите "Enter"\n')
    text = input('Напишите техт заметки и нажмите "Enter"\n')
    if os.path.exists('notes.csv'):
        db = Read_db()
        id = len(db) + 1
    else:
        with open("notes.csv", "w", encoding='utf-8') as file:
            id = 1
    note = f"{id}; {name}; {text}; {today}"
    with open("notes.csv", "a", encoding='utf-8') as file:
        file.write(f'{note}\n')
    file.close()
    print(f"\nЗаметка сохранена под номером {id}\n")


def Read_db():
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


Create_note()
