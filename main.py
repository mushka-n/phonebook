from checks_templates import Reveal_Data_Type
from Database import Database
from print import *

poss_commands = ['1', '2', '3', '4', '5', '6', '7', '0']
ud_temp = "Insert user's data \033[33m( id / name and (or) surname / phone / birth date )\033[0m:  "

db = Database()
db.Read_Database()

print("Possible commands:\n1 - Add new user\n2 - Print all data\n3 - Find user")
print("4 - Delete user(s)\n5 - Change user's information")
print("6 - Count user's age\n7 - Show users with closest birthdays\n0 - Exit")

while 1:
    command = input("Insert a command:  ")
    if command in poss_commands:
        if command == '1':
            db.New_User()
        elif command == '2':
            db.Print_All_Data()
        elif command == '3':
            userdata = input(ud_temp.format())
            db.Find_User(Reveal_Data_Type(userdata))
        elif command == '4':
            userdata = input(ud_temp.format())
            db.DeleteUser(Reveal_Data_Type(userdata))
        elif command == '5':
            userdata = input(ud_temp.format())
            db.ChangeUser(Reveal_Data_Type(userdata))
        elif command == '6':
            userdata = input(ud_temp.format())
            db.Count_Users_Age(Reveal_Data_Type(userdata))
        elif command == '7':
            db.Search_For_Close_Birthday()
        if command == '0':
            print_green("Bye")
            break
    else:
        print_red("Unknown command")
