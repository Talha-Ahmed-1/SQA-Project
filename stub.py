def wholeCode(res, color, width):
    clr = []                            #1
    wid = []                            #2
    res_ij = []                         #3
    for i in range(len(res)):           #4
        for j in range(len(res[i])):    #5
            if i % 2 == 0:              #6
                color = "honeydew3"     #7
            else:
                color = "white"         #8
            if j == 1:                  #9
                width = 15              #10
            else:
                width = 10              #11

            clr.append(color)           #12
            wid.append(width)           #13
            res_ij.append(res[i][j])    #14
            # Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)
    return [clr,wid,res_ij]             #15

            # Stub in form of return statement is replaced with label 
            # for testing purpose because label is a module of tkinter.

def driver():
    print("*****************")
    print("Path: 1 2 3 4 15")
    print("*****************")
    print(wholeCode([],None,None))
    print("*****************")
    print("Path: 1 2 3 4 5 4 15")
    print("*****************")
    print(wholeCode([()],None,None))
    print("*****************")
    print("Path: 1 2 3 4 5 6 7 9 10 12 13 14 5 4 15")
    print("***************************************************")
    print(wholeCode([(1, 'hello', 'test123')],None,None))
    print("***************************************************")
    print("Path: 1 2 3 4 5 6 7 9 11 12 13 14 5 4 15")
    print("***************************************************")
    print(wholeCode([(1, 'hello', 'test123')],None,None))
    print("***************************************************")
    print("Path: 1 2 3 4 5 6 8 9 11 12 13 14 5 4 15")
    print("***************************************************")
    print(wholeCode([(1, 'hello', 'test123'), (2, 'SQA', 'team')],None,None))
    print("********************************************************************")

def checkIfElse(color, width, i, j):
    if i % 2 == 0:
        color = "honeydew3"
    else:
        color = "white"
    if j == 1:
        width = 15
    else:
        width = 10
    return [color,width]

def checkNestedFor(res, color, width, i):
    for j in range(len(res[i])):
        if i % 2 == 0:
            color = "honeydew3"
        else:
            color = "white"
        if j == 1:
            width = 15
        else:
            width = 10

        return [color, width, res[i][j]]

def drive():

    print("---------------------------------If Else Statement--------------------------------------------")

    color = None
    width = None
    lst = [1,2,3,4]
    lst1 = [1,2,3,4]
    print("Checking IF/ELSE first.")
    for i in lst:
        for j in lst1:
            print(checkIfElse(color,width,i,j))
    
    print("---------------------------------Nested For Loop--------------------------------------------")
    
    print("Checking Nested For:")
    res = [(1, 'hello', 'test123'), (2, 'talha', 'ahmed')]

    print("Skip the for entirely:")
    print(checkNestedFor([()],None,None,0))
    print("Only one pass through the loop:")
    print(checkNestedFor([(0,)],None,None,0))
    print("Two passes through the loop:")
    print(checkNestedFor([(0,1)],None,None,0))
    print("Two passes through the loop:")
    for i in range(len(res)):
        print(checkNestedFor(res,color,width,i))

    print("---------------------------------Whole Block of Code--------------------------------------------")

    print("Checking Nested For:")
    res = [(1, 'hello', 'test123'), (2, 'talha', 'ahmed')]

    print("Skip the for entirely:")
    print(wholeCode([()],None,None))
    print("Only one pass through the loop:")
    print(wholeCode([(0,)],None,None))
    print("Two passes through the loop:")
    print(wholeCode([(0,1)],None,None))
    print("Two passes through the loop:")
    print(wholeCode(res,color,width))

if __name__ == "__main__":
    print("-----------------------------------Testing Independent Paths---------------------------------")
    driver()
    drive()