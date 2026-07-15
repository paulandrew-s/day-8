from addition import add, subtract, multiply, divide

def test_add_positive_numbers():

    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 5) == 5

def test_add_positive_and_negative():
    assert add(5, -3) == 2

def test_add_float():
    assert add(2.4, 3.2) == 5.6



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