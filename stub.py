def wholeCode(res, color, width):
    clr = []
    wid = []
    res_ij = []
    for i in range(len(res)):
        for j in range(len(res[i])):
            if i % 2 == 0:
                color = "honeydew3"
            else:
                color = "white"
            if j == 1:
                width = 15
            else:
                width = 10

            clr.append(color)
            wid.append(width)
            res_ij.append(res[i][j])
            # Label(fr, bg=color, width=width, font=("Arial", 15), text=res[i][j]).grid(row=i + 1, column=j)
    return [clr,wid,res_ij]

            # Stub in form of return statement is replaced with label 
            # for testing purpose because label is a module of tkinter.

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

def driver():

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
    driver()