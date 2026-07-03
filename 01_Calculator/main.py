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


while True:
    print("===" * 40)
    print("1. Addition \n2. Subtraction \n3. Multiplications \n4. Division \n5. Modulus \n6. Exponent calculations")
    operation = get_operation()

    print()

    match operation:
        case 1:
            print("You chose Addition : num1 + num2")
            num1, num2 = get_number()
            print("The addition of ", num1, "and", num2, " = ", add(num1, num2))

        case 2:
            print("you chose subtraction, num1 - num2")
            num1, num2 = get_number()
            print("The subtraction of ", num2, "from", num1, " = ", sub(num1, num2))

        case 3:
            print("You chose multiplication, num1 * num2")
            num1, num2 = get_number()
            print("The multiplication of ", num1, "and", num2, " = ", prod(num1, num2))

        case 4:
            print("You chose division :: num1 / num2")
            num1, num2 = get_number()
            if num2 == 0:
                print("Invalid operands")
            else:
                print("The division of ", num1, "by", num2, " = ", div(num1, num2))

        case 5:
            print("you chose to calculate remainder :: num1 % num2 ")
            num1, num2 = get_number()
            if num2 == 0:
                print("Invalid operands")
            else:
                print("The remainder of ", num1, "by", num2, " = ", mod(num1, num2))

        case 6:
            print("you chose exponent calculations, num1 ^ (num2)")
            num1, num2 = get_number()
            print("The power of ", num1, "to ", num2, " = ", expo(num1, num2))

    if ask_to_continue():
        continue
    break
