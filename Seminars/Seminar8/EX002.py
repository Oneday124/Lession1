# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчетство, номер телефона - данные, которые должны находиться в файле
# 1. Программа должна выводить данные
# 2. Программа должна сохраныть данные в текстовом формате
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (имя или фамилию)
# 4. Использование функций. Программа не должна быть линейной


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
            "1. Отобразить весь справочник\n"
            "2. Найти абонента по фамилии\n"
            "3. Найти абонента по номеру телефона\n"
            "4. Добавить абонента в справочник\n"
            "5. Сохранить справочник в текстовом формате\n"
            "6. Закончить работу")
    choice = int(input('Выберите пункт меню: '))
    return choice

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_phone_book('phon.txt')

    while choice != 6:
        if choice == 1:
            print_resuil(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user('phon.txt', user_data)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, 'phon.txt')
        choice = show_menu()

def print_resuil(phone_book):
    for item in phone_book:
        print(item, sep = '\n')

def read_phone_book(filename)-> list:                       # Чтение файла
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def get_search_name():
    name = input('Введите имя для поиска: ')
    return name

def find_by_name(phone_book, name):
    for item in phone_book:
        if name == item['Фамилия'] or name == item['Имя']:
            print(item)
    return work_with_phonebook()

def get_search_number():
    number = input('Введите номер телефона для поиска: ')
    return number

def find_by_number(phone_book, number):
    for item in phone_book:
        if number == item['Телефон']:
            print(item)
    return work_with_phonebook()

def get_new_user():
    new_user = ''
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    for i in fields:
        temp = input(f'Введите {i}: ')
        new_user += temp + ','
    return new_user

def add_user(phone_book, user_data):
    with open(phone_book, 'a', encoding='utf-8') as phone_book:
            phone_book.write(user_data + '\n')
    print('Контакт внесен в телефонную книгу')

def get_file_name():
    file_name = input('Введите имя файла: ')
    return file_name

def write_txt(file_name, phone_book):
    with open(phone_book, 'r', encoding='utf-8') as phone_book, \
            open(file_name + '.txt', 'a', encoding='utf-8') as file_name:
        for line in phone_book:
            file_name.write(line + '\n')
    print(f'Справочник успешно сохранен')

work_with_phonebook()

