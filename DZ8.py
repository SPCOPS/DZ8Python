# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.
# Показывает информацию в файле

def print_menu():
    print("""
    ------------------------------- \n
    1 - вывести все контакты  
    2 - поиск контакта
    3 - добавить контакт 
    4 - изменить данные контакта 
    5 - удалить контакт 
    6 - выход  
    ------------------------------- \n 
    """)
def addition():
    with open(file_path, 'a', encoding='utf8') as open_book:
        add_f = (input('Введите фамилию: ' ).title())
        add_i = (input('Введите имя: ' ).title())
        add_tel = (input('Введите телефон: ' ).title())
        new_line = add_f +' '+add_i +' '+ add_tel 
        open_book.writelines(f'\n{new_line}')
        print(new_line)
def search():
    with open(file_path, 'r', encoding='utf8') as open_book:
        search_param = (input('Введите параметр для поиска: ' ).title())
        for line in open_book:
            if search_param in line:
                print(line)
def remove_contact():
    with open(file_path, 'r', encoding="utf-8") as open_book:
        X = input('Введите имя или фамилию для удаления: ')
        lines = open_book.readlines()
        with open(file_path, 'w', encoding="utf-8") as open_book:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    open_book.write(line)
def edit():
    with open(file_path, 'r', encoding="utf-8") as open_book:
        search_param = (input('Введите параметр для поиска: ' ).title())
        with open (file_path, 'w', encoding='utf8') as open_book:
            for line in search_param:
                if search_param in line:
                    print(line)
                    add_f = (input('Введите фамилию: ' ).title())
                    add_i = (input('Введите имя: ' ).title())
                    add_tel = (input('Введите телефон: ' ).title())
                    new_line = add_f +' '+add_i +' '+ add_tel + '\n'
                    line = line.replace(line, new_line)
                open_book.writelines(line)
def read_all():
    with open(file_path, 'r', encoding='utf8') as open_book:
        print()
        for line in open_book:
            print(line)  
def tasks(task):
   if task > 6: print('Ошибка в номере задачи!')
   if task == 6: print('До встречи!')
   else:
    match task:
        case 1: # вывести все контакты
            read_all()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))   
        case 2: # поиск контактов
            search()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 3: # добавить контакт
            addition()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 4: # изменить контакт
            edit()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: ')))
        case 5: # удалить контакт
            remove_contact()
            print_menu()
            tasks(int(input('Введите номер задачи от 1 до 6: '))) 
import os
import sys           
file_path = os.path.join(os.path.dirname(sys.argv[0]), 'phon.txt')
print_menu()
tasks(int(input('Введите номер задачи от 1 до 6: ')))
# def show_data(filename):
#     print("\nПП | ФИО | Телефон")
#     with open(filename, «r», encoding=»utf-8″) as data:
#     print(data.read())
#     print(«»)

# # Записывает информацию в файл
# def export_data(filename):
# with open(filename, «r», encoding=»utf-8″) as data:
# tel_file = data.read()
# num = len(tel_file.split(«\n»))
# with open(filename, «a», encoding=»utf-8″) as data:
# fio = input(«Введите ФИО: «)
# phone_number = input(«Введите номер телефона: «)
# data.write(f»{num} | {fio} | {phone_number}\n»)
# print(f»Добавлена запись : {num} | {fio} | {phone_number}\n»)

# # Изменяет информацию из файла
# def edit_data(filename):
# print(«\nПП | ФИО | Телефон»)
# with open(filename, «r», encoding=’utf-8′) as data:
# tel_book = data.read()
# print(tel_book)
# print(«»)
# index_delete_data = int(input(«Введите номер строки для редактирования: «)) — 1
# tel_book_lines = tel_book.split(«\n»)
# edit_tel_book_lines = tel_book_lines[index_delete_data]
# elements = edit_tel_book_lines.split(» | «)
# fio = input(«Введите ФИО: «)
# phone = input(«Введите номер телефона: «)
# num = elements[0]
# if len(fio) == 0:
# fio = elements[1]
# if len(phone) == 0:
# phone = elements[2]
# edited_line = f»{num} | {fio} | {phone}»
# tel_book_lines[index_delete_data] = edited_line
# print(f»Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n»)
# with open(filename, «w», encoding=’utf-8′) as f:
# f.write(«\n».join(tel_book_lines))

# # Удаляет информацию из файла
# def delete_data(filename):
# print(«\nПП | ФИО | Телефон»)
# with open(filename, «r», encoding=»utf-8″) as data:
# tel_book = data.read()
# print(tel_book)
# print(«»)
# index_delete_data = int(input(«Введите номер строки для удаления: «)) — 1
# tel_book_lines = tel_book.split(«\n»)
# del_tel_book_lines = tel_book_lines[index_delete_data]
# tel_book_lines.pop(index_delete_data)
# print(f»Удалена запись: {del_tel_book_lines}\n»)
# with open(filename, «w», encoding=’utf-8′) as data:
# data.write(«\n».join(tel_book_lines))

# def main():
# my_choice = -1
# file_tel = «tel.txt»

# # Создает файл если его нет в папке
# with open(file_tel, «a», encoding=»utf-8″) as file:
# file.write(«»)

# while my_choice != 0:
# print(«Выберите одно из действий:»)
# print(«1 — Вывести инфо на экран»)
# print(«2 — Произвести экпорт данных»)
# print(«3 — Произвести изменение данных»)
# print(«4 — Произвести удаление данных»)
# print(«0 — Выход из программы»)
# action = int(input(«Действие: «))
# if action == 1:
# show_data(file_tel)
# elif action == 2:
# export_data(file_tel)
# elif action == 3:
# edit_data(file_tel)
# elif action == 4:
# delete_data(file_tel)
# else:
# my_choice = 0

# print(«До свидания»)

# if __name__ == «__main__»:
# main()