
from pathlib import Path

FILE_PATH = Path('phonebook.txt')
print(FILE_PATH)

def open_contakt():
    with open(FILE_PATH, 'a', encoding='utf8') as file:
        info=input('Введите данные: ')
        file.write(f'\n{info}')

def show_contakt():
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        # print([lines for lines in file])
        # print(file.readlines())
        print(*[line for line in file])

def find_contakt():
    list_1=[]
    serch = input('Введите скомое: ').strip()
    with open(FILE_PATH, 'r', encoding='utf8') as file:
        for contact in file:
            if serch in contact:
                list_1.append(contact)
        print(*[line for line in list_1])


def edit_contakt():
    print("\nФИО;Телефон")
    with open(FILE_PATH, "r", encoding='utf-8') as data:
        tel_book = data.read()
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(";")
    fio = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    if len(fio) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
    edited_line = f"{fio};{phone}"
    tel_book_lines[index_delete_data] = edited_line
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(FILE_PATH, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

def delete_contakt():
    print("\nФИО;Телефон")
    with open(FILE_PATH, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book)
    print("")
    index_delete_contakt = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_contakt]
    tel_book_lines.pop(index_delete_contakt)
    print(f"Удалена запись: {del_tel_book_lines}\n")
    with open(FILE_PATH, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))

def choouse():
    flag=True
    while flag:
        n=input('Выберите действие: ')
        match n:
            case '1':
                open_contakt()  
            case '2':
                show_contakt()  
            case '3':
                find_contakt()  
            case '4':
                edit_contakt()  
            case '5':
                delete_contakt() 
            case '0':
                flag=False
                
choouse()