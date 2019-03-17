#integer calculator
a = int(input("input first number: "))
b = int(input("input second number number: "))
print(" ")
op = int(input("choose an operation (1=add, 2=subtract, 3=multiply): "))
if op == 1:
    print("-----------------------------------------")
    print("The sum of ",a," and ",b, "is = ", a+b)
elif op == 2:
    print("-----------------------------------------")
    print(" ")
    print(a,"-",b, "(choice one)       or      ", b,"-",a, "(choice two)")
    order = int(input("Select choice (1) or choice (2): "))
    if order == 1:
        print("-----------------------------------------")
        print(a, "-", b, "is = ", a-b )
    elif order == 2:
        print("-----------------------------------------")
        print(b, "-", a, "is = ", b-a)
    else:
        print("INVALID CHOICE")
elif op == 3:
    print("-----------------------------------------")
    print("The product of ", a, " and ", b, " is =  ", a*b)
else:
    print("INVALID OPERATION")
print(" ")
print("AHMED'S CALCULATOR")

exit = input("ANY KEY TO EXIT...")
