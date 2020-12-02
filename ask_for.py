from checks_templates import *
from print import print_red


# Ввод и имени и фамилии и проверка на нужное кол-во вводимых слов
def Ask_For_Nasu():
    nasu = list(input("\tInsert user's name and surname:  ").split())
    while len(nasu) != 2:
        if len(nasu) > 2:
            print_red("\t\tOnly name and surname should be provided")
            nasu = list(input("\t\tChange inserted value:  ").split())
        elif len(nasu) < 2:
            print_red("\t\tYou should provide both name and surname")
            nasu = list(input("\t\tChange inserted value :  ").split())

    name = nasu[0]
    surname = nasu[1]

    # Проверка имени и фамилии на наличие кириллицы
    while not NaSu_IsValid(name) or len(name) > 25:
        if not NaSu_IsValid(name): print_red("\t\tReceived name is invalid. Latin symbols only")
        if len(name) > 25: print_red("\t\tReceived name is too long")
        name = input("\t\tChange inserted name :  ")
    while not NaSu_IsValid(surname) or len(surname) > 25:
        if not NaSu_IsValid(name): print_red("\t\tReceived surname is invalid. Latin symbols only")
        if len(surname) > 25: print_red("\t\tReceived surname is too long")
        surname = input("\t\tChange inserted surname :  ")
    name, surname = NaSu_Template(name, surname)

    return name, surname


# Ввод и телефона и проверка на валидность
def Ask_For_Phone():
    phone = input("\tInsert user's phone:  ")
    while not Phone_IsValid(phone):
        print_red("\t\tReceived phone number is invalid")
        phone = input("\t\tChange inserted phone number:  ")
    phone = Phone_Template(phone)
    return (phone)


# Ввод даты и подравниевание под нужный формат
def Ask_For_Birth_Date():
    dmy_format_first = "\tInsert users birth date in 'DD MM YYYY' format'\033[33m(Enter nothing to skip)\033[0m:  "
    dmy_format = "\t\tChange inserted birth date \033[33m(Enter nothing to skip)\033[0m:  "
    dmy = (input(dmy_format_first.format()))
    while not BirthDate_IsValid(dmy):
        print_red("\t\tGiven birth date is invalid")
        dmy = (input(dmy_format.format()))
        if dmy == '': break

    if dmy == '':
        return '--/--/----'
    else:
        return BirthDate_Template(dmy)


# Ввод id пользователей
def Ask_For_Users(ids):
    wrong_data = 1
    users = []
    while wrong_data:
        wrong_data = 0
        users = list(input("\tChoose id(s) of user(s) that you want to continue operating with:  ").split())
        if users == ['*']:
            users = ids
            break
        for i in range(len(users)):
            try:
                users[i] = int(users[i])
                if users[i] - 1 not in ids:
                    print_red("\t\tChoose between given ids")
                    wrong_data = 1
                    i -= 1
            except ValueError:
                print_red("\t\tOnly numbers should be provided")
                wrong_data = 1
                i -= 1
    return users


# Ввод информации для измения
def Ask_For_Info():
    types = ["full name", "phone", "birth date"]
    info = input("\tInsert name of information that you want to change: ")
    while info not in types:
        print_red("\t\tUnknown information type")
        print("\t\tPossible variants: 'full name', 'phone', 'birth date' ")
        info = input("\t\tChange provided information type: ")
    return info
