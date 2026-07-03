print("Hello Guys, you are free to do as much as calculations you want to do..... ")
print("Among the following operations , what do you want to do...")

while(True):
    print("==="*40)
    print("1. Addition \n2. Subtraction \n3. Multiplications \n4. Division \n5. Modulus \n6. Exponent calculations")
    operation = int(input("\nEnter what operations you want me to preform::")) 

    def add(a, b):
        return a + b
    def sub(a, b):
        return a-b
    def prod(a, b):
        return a*b
    def div(a , b):
        return a / b
    def mod(a,b):
        return a%b
    def expo(a , b):
        return a**b

    if operation > 0 and operation <7 :
        print("Operation is valid")
    else: 
        print("Opertion invalid")

    def get_number():
        num1 = float(input("Enter the first number: num1 = "))
        num2 = float(input("Enter the second number: num 2 ="))
        return (num1, num2)

    match operation:
        case 1:
            print("You chose Addition : num1 + num2")
            num1, num2 = get_number()
            print("The addition of ", num1, "and", num2," = ",add(num1, num2))

        case 2:
            print("you chose subtraction, num1 - num2")
            num1, num2 = get_number()
            print("The subtraction of ", num2, "from", num1," = ",sub(num1, num2))
            
        case 3:
            print("You chose multiplication, num1 * num2")
            num1, num2 = get_number()
            print("The multiplication of ", num1, "and", num2," = ",prod(num1, num2))
        case 4:
            print("You chose division :: num1 / num2")
            num1, num2 = get_number()
            if(num2 == 0):
                print("Invalid operands")
            else:
                print("The division of ", num1, "by", num2," = ",div(num1, num2))
        case 5:
            print("you chose to calculate reminder :: num1 % num2 ")
            num1, num2 = get_number()
            print("The reminder of ", num1, "by", num2," = ",mod(num1, num2))
        case 6:
            print("you chose exponent calculations,num1 ^ (num2)")
            num1, num2 = get_number()
            print("The power of ", num1, "to ", num2," = ", expo(num1, num2))
    print("Do you want to do another calculation?[Y/N]")
    conditions = input("Enter yes or no :")
    if conditions == 'N':
        print("Further calculations is not required!!!")
        break
    
        




