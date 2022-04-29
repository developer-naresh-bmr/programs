first=int(input("Enter first number:"))
second=int(input("Enter second number:"))
print()
print("MENU")
print("1.addition\n 2.subtraction\n 3.multiplication\n 4.division\n 5.modulus\n 6.exit\n")
operator=int(input("choose your option(1-6):"))

def addition(x,y):
    return first+second
def subtraction(x,y):
    return first-second
def multiplication(x,y):
    return first*second
def division(x,y):
    return first/second
def modulus(x,y):
    return first%second


if operator==1:
    print(addition(first,second))
elif operator==2:
    print(subtraction(first,second))
elif operator==3:
    print(multiplication(first,second))
elif operator==4:
    print(division(first,second))
elif operator==5:
    print(modulus(first,second))
else:
    print("Invalid option!!!")
