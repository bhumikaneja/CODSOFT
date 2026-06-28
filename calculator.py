print("===== CALCULATOR PROGRAM =====")

while True:

    first_num = float(input("Enter first value: "))
    second_num = float(input("Enter second value: "))

    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    option = input("Select option (1-4): ")

    if option == "1":
        answer = first_num + second_num
        print("Answer =", answer)

    elif option == "2":
        answer = first_num - second_num
        print("Answer =", answer)

    elif option == "3":
        answer = first_num * second_num
        print("Answer =", answer)

    elif option == "4":
        if second_num != 0:
            answer = first_num / second_num
            print("Answer =", answer)
        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid option selected.")

    repeat = input("\nDo another calculation? (yes/no): ")

    if repeat.lower() != "yes":
        print("Calculator closed.")
        break