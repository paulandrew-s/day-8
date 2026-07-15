def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input('Enter your choice: '))

    num1, num2 = [float(x) for x in input('Enter two numbers: ')]

    if choice == 1:
        print('The result of addition is: ', add(num1, num2))
    elif choice == 2:
        print('The result of subtraction is: ', subtract(num1, num2))
    elif choice == 3:
        print('The result of multiplication is: ', multiply(num1, num2))
    elif choice == 4:
        print('The result of division is: ', divide(num1, num2))
    else:
        print('Invalid choice')


if __name__ == "__main__":
    main()