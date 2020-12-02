from ask_for import Ask_For_Users


# Поиск по массиву
def Search_In_Arr(arr, x):
    result = []
    for i in range(len(arr)):
        if x == arr[i]:
            result.append(i)
    return result


# Запрос пользователей (если нужно)
def Users(ids):
    if len(ids) > 1:
        users = Ask_For_Users(ids)
    elif len(ids) == 0:
        users = []
    else:
        users = [ids[0]+1]
    return users
