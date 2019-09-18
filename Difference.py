def pure_check(listpos, listneg):
    list_difference = []
    for i in listpos + listneg:
        if i > 0:
            if i not in listpos or -i not in listneg:
                list_difference.append(i)
        else:
            if -i not in listpos or i not in listneg:
                list_difference.append(i)

    return list_difference
