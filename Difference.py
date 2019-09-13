def Diff(truthvalues, listpos, listneg):
    list_difference = [i for i in listpos + listneg if (i not in listpos or -i not in listneg) or (-i not in listpos
                                                                                                   or i not in listneg)]
    for literal in list_difference:
        truthvalues[literal] = 1
        truthvalues[-literal] = 0
    return list_difference