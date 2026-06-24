def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def div(a,b):
    if b==0:
        return "cannot divide by zero"
    return a/b


print("1.ADD")
print("2.SUBTRACT")
print("3.MULTIPLY")
print("4.DIVIDE")
print("5.EXIT")


while True:
    
    choice=int(input("ENTER YOUR CHOICE (1/2/3/4):"))

    num1=float(input("ENTER FIRST NUMBER :"))
    num2=float(input("ENTER SECOND NUMBER:"))

    if choice ==1:
        print("RESULT:", sum(num1,num2))

    elif choice == 2:
        print("RESULT:",sub(num1,num2))
    
    elif choice == 3:
        print("RESULT:",mul(num1,num2))

    elif choice == 4:
        print("RESULT:",div(num1,num2))

    elif choice ==5:
        print("THANKS FOR USING THIS CALCULATOR")
        break
    else:
        print("INVALID")
    
    


