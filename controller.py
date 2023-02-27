import db, gui
from datetime import datetime

def button_click():
    a = gui.Choice()
    if (a == 1):
        
        id = gui.id_input()
        name = gui.Name_input()
        description = gui.Description_input()
        print("Вы хотите использовать txt (1) или csv (2) формат, или json (3):")
        flag = int(input())
        while ((flag < 1) & (flag > 3)):
            flag = int(input())
            print("Введены некорректные данные, попробуйте снова: ")
        current_datetime = str(datetime.now())
        if flag == 1:
            print("В данной версии приложения данный формат не доступен")
        elif flag == 2: 
            print
        else:
            db.Saving_json(id, name, description, current_datetime)

    elif (a == 2):
        print("Вы хотите использовать txt (1), csv (2) формат или json (3):")
        flag = int(input())
        while ((flag < 1) & (flag > 3)):
            flag = int(input())
            print("Введены некорректные данные, попробуйте снова: ")
        if flag == 1:
            print("В данной версии приложения данный формат не доступен")
        elif flag == 2:
            print("В данной версии приложения данный формат не доступен")
        elif flag == 3:
            db.get_base_json_names() 
        else: 
            print("Введены некорректные данные")
    elif(a == 3):
        print("Введите id заметки, которую хотите прочитать")
        id_found = int(input())
        db.get_base_json_description(id_found)
    elif(a == 4):
        print("Введите id заметки, которую хотите редактировать")
        id_found = int(input())
        db.editing_json(id_found)
    elif(a == 5):
        print("Введите id заметки, которую хотите удалить")
        id_found = int(input())
        db.deleting_json(id_found)
