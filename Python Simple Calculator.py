#Python Simple Project

def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
    
def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a,b):
    answer = a*b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a,b):
    answer = a/b
    print(str(a) + " + " + str(b) + " = " + str(answer))
while True: 
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Input you choice: ")
    if choice == "1":
        print("Addition")
        a = int(input("Enter first Number: "))
        b = int(input("Enter first Number: "))
        add(a,b)
    elif choice == "2":
        print("Subtraction")
        a = int(input("Enter first Number: "))
        b = int(input("Enter first Number: "))
        sub(a,b)
    elif choice == "3":
        print("Multiplication")
        a = int(input("Enter first Number: "))
        b = int(input("Enter first Number: "))
        mul(a,b)
    elif choice == "4":
        print("Division")
        a = int(input("Enter first Number: "))
        b = int(input("Enter first Number: "))
        div(a,b)
    elif choice == "5" :
        print("Calculator Exiting")   
        quit()
