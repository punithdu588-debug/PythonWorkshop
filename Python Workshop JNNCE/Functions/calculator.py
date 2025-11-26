from operator import truediv


def userInput():
    first_input=int(input("Enter the First number"))
    second_input=int(input("Enter the second  Number"))

    return first_input,second_input

def add(a=0,b=0):
    return a+b

def sub(a=0,b=0):
    return a-b

def mult(a=0,b=0):
    return a*b

def div(a=0,b=0):
    return a/b

print("Welcome to cal")
while True:
    print("Select the choose :\n1:Add\n2:sub\n3:mult\n4:div\n5:stop")
    choose=int(input("Enter the choose"))

    if choose==1:
        x,y=userInput()
        print(f"addition  of two number:{add(x, y)}")

    elif choose == 2:
        x, y = userInput()
        print(f"subtraction of two number:{sub(x, y)}")

    elif choose == 3:
        x, y = userInput()
        print(f"multiplication of two number:{mult(x, y)}")

    elif choose == 4:
        x, y = userInput()
        print(f"Division of two number:{div(x, y)}")


    elif choose == 4:
      print("Thank You for using calculate")


