print("=== Simple Calculator ===")

while True:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Answer:", num1 + num2)
    elif operator == "-":
        print("Answer:", num1 - num2)
    elif operator == "*":
        print("Answer:", num1 * num2)
    elif operator == "/":
        if num2 != 0:
            print("Answer:", num1 / num2)
        else:
            print("You can't divide by zero!")
    else:
        print("Invalid operator!")

    again = input("Do another calculation? (yes/no): ")

    if again.lower() != "yes":
        print("Thank you for using the calculator!")
        break