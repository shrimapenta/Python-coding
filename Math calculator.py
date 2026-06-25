print("1. Square")
print("2. Sqaure root")
print("3. Addition")
print("4. Subtraction")
print("5. Multiplication")
print("6. Division")
print("7. Powers")
print("8. Modulus")
operation = input("Enter your operation (1-8): ")
if operation=="1":
    num=int(input("Enter a number: "))
    print("Answer = ",num ** 2)
elif operation=="2":
    num=int(input("Enter a number: "))
    import math
    print("Answer = ",math.sqrt(num))
else:
    num1=int(input("Enter your first number: "))
    num2=int(input("Enter your second number: "))
    if operation=="3":
        print("Answer = ",num1+num2)
    elif operation=="4":
        print("Answer = ",num1-num2)
    elif operation=="5":
        print("Answer = ",num1*num2)
    elif operation=="6":
        print("Answer = ",num1/num2)
    elif operation=="7":
        print("Answer = ", num1**num2)
    elif operation=="8":
        print("Answer = ",num1%num2)