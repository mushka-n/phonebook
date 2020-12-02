import re
import datetime

# Возвращает тип данных полученной строки
def Reveal_Data_Type(userdata):
    if Phone_IsValid(userdata):
        return "phone", Phone_Template(userdata)

    try:
        return ['id', int(userdata)]
    except ValueError:
        pass

    if BirthDate_IsValid(userdata):
        return "birth date", BirthDate_Template(userdata)

    nasu = userdata.split()
    nasulen = len(nasu)
    if nasulen <= 2:
        if nasulen == 1 and NaSu_IsValid(nasu[0]):
            return "name or surname", NaSu_Template(nasu[0], 'Null')
        elif NaSu_IsValid(nasu[0]) and NaSu_IsValid(nasu[1]):
            return "full name", NaSu_Template(nasu[0], nasu[1])

    return 0


####################################

# Проверка на правильность имени и фамилии
def NaSu_IsValid(nasu):
    nasu_re = r'^[A-Za-z_]*[A-Za-z][A-Za-z_]*$'
    if re.match(nasu_re, nasu) is not None:
        return 1
    else:
        return 0


# Подгонка имени и фамилии под образец
def NaSu_Template(name, surname):
    name = name[0].upper() + name[1:]
    surname = surname[0].upper() + surname[1:]
    return name, surname


####################################

# Проверка на правильность телефона
def Phone_IsValid(phone):
    phone_re = r"(\+7|8|7).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})"
    if re.match(phone_re, phone) is None:
        return 0
    else:
        return 1


# Подгонка телефона под образец
def Phone_Template(phone):
    phone_template = ['+', '7', ' ', '(', 'X', 'X', 'X', ')', ' ', 'X', 'X', 'X', '-', 'X', 'X', '-', 'X', 'X']
    phone_template_indexes = [4, 5, 6, 9, 10, 11, 13, 14, 16, 17]
    right_phone_nums = re.findall(r'[0-9]', phone)
    for i in range(1, 11): phone_template[phone_template_indexes[i - 1]] = right_phone_nums[i]
    phone = ""
    for i in range(18): phone += phone_template[i]
    return phone


####################################

# Проверка на правильность даты рождения
def BirthDate_IsValid(dmy):
    if dmy == "": return 1

    dmy_re = r' |\/|\.|\-'
    dmy_min = datetime.date(year=1900, month=1, day=1)
    dmy_max = datetime.datetime.now().date()

    dmy = re.split(dmy_re, dmy)

    for i in range(3):
        try:
            dmy[i] = int(dmy[i])
        except:
            return 0

    try:
        if (dmy_min < datetime.date(year=dmy[2], month=dmy[1], day=dmy[0]) <= dmy_max):
            return 1
    except ValueError:
        return 0


# Подгонка даты рождения под образец
def BirthDate_Template(dmy):
    dmy_re = r' |\/|\.|\-'
    dmy = re.split(dmy_re, dmy)
    if len(dmy[0]) < 2:
        dmy[0] = '0' + dmy[0]
    if len(dmy[1]) < 2:
        dmy[1] = '0' + dmy[1]
    dmy = dmy[0] + '/' + dmy[1] + '/' + dmy[2]
    return dmy
