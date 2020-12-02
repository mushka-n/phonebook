from ask_for import *
from funcs import Search_In_Arr, Users
from print import *
import datetime
import math


class Database:
    currid = 0
    names = []
    surnames = []
    phones = []
    birth_dates = []

    now = datetime.datetime.today().date()

    # Считывание содержимого текстового файла
    @staticmethod
    def Read_Database():
        datafile = open('data.txt', 'r+')
        lines = datafile.readlines()
        linesnum = len(lines)
        if linesnum < 2:
            datafile.write(" Id:   | Name:                     | Phone:             | Birth date:\n")
            datafile.write("#######|###########################|####################|############")
            return
        else:
            for i in range(2, linesnum - 1):
                data = lines[i].split()
                if len(data) > 5:
                    name = data[2]
                    if lines[i + 1][0] != '-':
                        surname = lines[i + 1][1]
                        i += 1
                    else:
                        surname = data[3]
                    phone = data[-5] + ' ' + data[-4] + ' ' + data[-3]
                    birth_date = data[-1]
                    Database.currid += 1
                    Database.names.append(name)
                    Database.surnames.append(surname)
                    Database.phones.append(phone)
                    Database.birth_dates.append(birth_date)
        datafile.close()
        return

    # Перезагрузка текстового файла
    @staticmethod
    def ReloadDatabase():
        open('data.txt', 'w').close()
        datafile = open('data.txt', 'a+')
        datafile.write(" Id:   | Name:                     | Phone:             | Birth date:\n")
        datafile.write("#######|###########################|####################|############")
        for i in range(Database.currid):
            id = str(i + 1)
            name = Database.names[i]
            surname = Database.surnames[i]
            phone = Database.phones[i]
            birth_date = Database.birth_dates[i]
            data = id + (' ' * (5 - len(id))) + ' | '
            if len(name) + len(surname) + 1 > 25:
                data += name + (' ' * (25 - len(name))) + ' | ' + phone + ' | ' + birth_date
                data += "\n       | " + surname + (' ' * (25 - len(surname))) + ' | ' + (' ' * 18) + ' | '
            else:
                data += name + ' ' + surname + (
                        ' ' * (24 - len(name) - len(surname))) + ' | ' + phone + ' | ' + birth_date
            datafile.write("\n " + data + '\n' + ('-' * 69))
        datafile.close()
        return

    # Находит, выводит и выовращает id пользователя(ей)
    @staticmethod
    def Find_Print_Return(userdata):
        if userdata == 0:
            print_red("\tError in given values")
            return 0
        elif Database.currid == 0:
            print_red('\t Database is empty')
            return 0

        type, data = userdata[0], userdata[1]
        ids = Database.Search_By_Data(type, data)
        Database.Print_By_Ids(ids, type)
        users = Users(ids)
        return users

    # Поиск пользоватля(ей) по базе данных
    @staticmethod
    def Search_By_Data(type, data):
        ids = []
        if type == "id":
            ids.append(data - 1)
        elif type == "name or surname":
            names = Search_In_Arr(Database.names, data[0])
            surnames = Search_In_Arr(Database.surnames, data[0])
            ids = list(set(names + surnames))
        elif type == "full name":
            names = Search_In_Arr(Database.names, data[0])
            surnames = Search_In_Arr(Database.surnames, data[1])
            for i in range(len(min(names, surnames))):
                if names[i] == surnames[i]:
                    ids.append(names[i])
        elif type == "phone":
            ids = Search_In_Arr(Database.phones, data)
        elif type == "birth date":
            ids = Search_In_Arr(Database.birth_dates, data)

        return ids

    # Вывод нескольких пользователей по их id
    @staticmethod
    def Print_By_Ids(ids, type):
        lenIds = len(ids)
        if lenIds == 1:
            print("\tThere is 1 person in database with given", type, ":")
        else:
            print("\tThere are", lenIds, "people in database with given", type, ":")
        print("\t##########################################################")

        for i in range(lenIds):
            print("\tId:         ", ids[i] + 1)
            print("\tName:       ", Database.names[ids[i]])
            print("\tSurname:    ", Database.surnames[ids[i]])
            print("\tPhone:      ", Database.phones[ids[i]])
            print("\tBirth date: ", Database.birth_dates[ids[i]])
            print("\t----------------------------------------------------------")

    ##################################

    # Добавление нового пользователя
    def New_User(self):

        # Открытие файла для добавления инф-ии
        datafile = open('data.txt', 'a+')

        name, surname = Ask_For_Nasu()
        phone = Ask_For_Phone()
        birth_date = Ask_For_Birth_Date()

        add = 0
        if phone not in Database.phones:
            if name in Database.names and surname in Database.surnames:
                uformat = "\t\t\033[33m(Enter nothing to decline)\033[0m:  "
                print_red("\t\tUser with similar name or surname exists")
                print("\t\tDo you still want to create new user?")
                answer = input(uformat.format())
                if answer != '':
                    add = 1
            else:
                add = 1
        else:
            print_red("\tUser with that number already exists")

        if add == 1:
            Database.currid += 1
            Database.names.append(name)
            Database.surnames.append(surname)
            Database.phones.append(phone)
            Database.birth_dates.append(birth_date)
            Database.ReloadDatabase()
            print_green("New user is added!")

        datafile.close()
        return

    # Вывод справочника на экран
    @staticmethod
    def Print_All_Data():
        datafile = open('data.txt', 'r')
        for line in datafile:
            print('\t' + line, end="")
        print()
        datafile.close()
        return

    # Поиск пользователя по заданной информации
    @staticmethod
    def Find_User(userdata):
        Database.Find_Print_Return(userdata)
        return

    # Удаление пользователя по заданной информации
    def DeleteUser(self, userdata):
        usersToDelete = Database.Find_Print_Return(userdata)
        if usersToDelete == 0: return

        for i in range(len(usersToDelete)):
            user = usersToDelete[i] - 1
            del Database.names[user]
            del Database.surnames[user]
            del Database.phones[user]
            del Database.birth_dates[user]
            Database.currid -= 1

        if len(usersToDelete) > 0:
            print_green("\tDelete operation was completed")
        else:
            print_red("There are no found users to delete")

        Database.ReloadDatabase()
        return

    # Изменение пользователя по заданной информации
    def ChangeUser(self, userdata):
        usersToChange = Database.Find_Print_Return(userdata)
        if usersToChange == 0: return

        for i in range(len(usersToChange)):
            info = Ask_For_Info()
            user = usersToChange[i] - 1
            if info == "full name":
                name, surname = Ask_For_Nasu()
                Database.names[user] = name
                Database.surnames[user] = surname
            elif info == "phone":
                phone = Ask_For_Phone()
                Database.phones[user] = phone
            elif info == "birth date":
                birth_date = Ask_For_Birth_Date()
                Database.birth_dates[user] = birth_date

        if len(usersToChange) > 0:
            print_green("\tChange operation was completed")
        else:
            print_red("There are no found users to change")

        Database.ReloadDatabase()
        return

    # Подсчет возраста пользователя
    @staticmethod
    def Count_Users_Age(userdata):
        usersToCountAge = Database.Find_Print_Return(userdata)
        if usersToCountAge == 0: return

        for i in range(len(usersToCountAge)):
            user = usersToCountAge[i] - 1
            print('\t' + Database.names[user], Database.surnames[user], ' - ', end=' ')
            if Database.birth_dates[user] == "--/--/----":
                print_red("that user's birth date is not set")
            else:
                dmy = list(map(int, Database.birth_dates[user].split('/')))
                bd = datetime.date(dmy[2], dmy[1], dmy[0])
                diff = Database.now - bd
                age = (diff.days + diff.seconds / 86400) / 365.2425
                print(math.trunc(age), "full years")

    # Вывод пользователей с ближайшим днем рождения (1 месяц)
    @staticmethod
    def Search_For_Close_Birthday():
        for i in range(Database.currid):
            if Database.birth_dates[i] != "--/--/----":
                dmy = list(map(int, Database.birth_dates[i].split('/')))
                now = datetime.date(2000, Database.now.month, Database.now.day)
                border = now + datetime.timedelta(1 * 365 / 12)
                if dmy[0] > 2 and dmy[1] == 12:
                    user = datetime.date(2000, dmy[1], dmy[0])
                else:
                    user = datetime.date(border.year, dmy[1], dmy[0])
                if now <= user <= border:
                    print("\t" + Database.names[i] + ' ' + Database.surnames[i], ' - ', user.day, '/', user.month,
                          sep='')
        return
