print("Hello guys, you are free to do as many calculations as you want to do..... ")
print("Among the following operations, what do you want to do...")


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def prod(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def expo(a, b):
    return a ** b


def get_number():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numbers only.")


def get_operation():
    while True:
        try:
            operation = int(input("\nEnter what operation you want me to perform: "))
            if 1 <= operation <= 6:
                return operation
            print("Operation invalid")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")


def ask_to_continue():
    while True:
        conditions = input("Do you want to do another calculation? [Y/N]: ").strip().lower()
        if conditions == 'y':
            return True
        if conditions == 'n':
            print("Further calculations are not required!!!")
            return False
        print("Invalid choice")


operations = {
    1: ('Addition', '+', add),
    2: ('Subtraction', '-', sub),
    3: ('Multiplication', '*', prod),
    4: ('Division', '/', div),
    5: ('Modulus', '%', mod)
}

while True:
    print("===" * 40)
    print("1. Addition \n2. Subtraction \n3. Multiplications \n4. Division \n5. Modulus \n6. Exponent calculations")
    operation = get_operation()

    print()

    if operation in operations:
        label, symbol, function = operations[operation]
        print(f"You choose {label} : num1 {symbol} num2")
        num1, num2 = get_number()
        if operation in (4, 5) and num2 == 0:
            print("Invalid operands")
        else:
            print(f"{num1} {symbol} {num2} = {function(num1, num2)}")
    elif operation == 6:
        print("you chose exponent calculations, num1 ^ num2")
        num1, num2 = get_number()
        if num1 < 0 and not num2.is_integer():
            print("Invalid operation: negative number to a fractional power gives a complex result.")
        elif num1 == 0 and num2 < 0:
            print("Invalid operation: zero cannot be raised to a negative power.")
        else:
            print(f"{num1} ^ {num2} = {expo(num1, num2)}")

    if ask_to_continue():
        continue
    break
