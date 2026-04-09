
print(" My Calculator")

while True:
    print("1- Add")
    print("2- Subtract")
    print("3- Multiply")
    print("4- Divide")
    print("5- Mod")
    print("6- Power")
    print("7- Square root")
    print("8- Exit")

    choice = input("Enter choice(: ")

    if choice == "8":
        break

    if choice == "7":
        num = float(input("Enter number(: "))
        if num >= 0:
            print("Result =" + str(num))
        else:
            print("Error")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result =", num1 + num2)

    elif choice == "2":
        print("Result =", num1 - num2)

    elif choice == "3":
        print("Result =", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error")

    elif choice == "5":
        print("Result =", num1 % num2)

    elif choice == "6":
        print("Result =", num1 ** num2)

    else:
        print("Wrong choice")
