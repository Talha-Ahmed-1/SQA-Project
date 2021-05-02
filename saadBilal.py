def code1(lstP, idd, passwordd):
    sch = [] #1
    valid = None #2
    for i in lstP: # list #3
        lst = list(i.split(" ")) #4
        sch.append(lst)#5
    for j in sch: #6                                    #[['123', '123'], ['talha', 'talha']]  j=['123', '123']
        if idd==j[0] and passwordd==j[1]: #7
            valid = True #8
            break 
        else: 
            valid = False #9

    return valid #10


lstP = ["123 123","talha talha"]
a = code1(lstP, "talha","talha")
print(a)