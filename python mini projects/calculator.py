def add(num1, num2):
    print(num1 + num2)

def sub(num1, num2):
    print(num1 - num2)
def quotient(num1, num2):
    print(num2 / num1)

def multi(num1, num2):
    print(num1 * num2)


def calculator(): 
    while True:
        num1 = str(input("Enter a number enter q to quit: "))
        operator = input("Enter operator (+, -, /, *, **, sqrt) enter q to quit: ")
        num2 = str(input("Enter number enter q to quit:"))
        if num1 == 'q':
            break
        elif num2 == 'q':
            break
        elif operator == 'q':
            break
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print("Invalid Integer")
        except TypeError:
            print("Invalid integer")
        try:
            if operator == '+':
                add(num1, num2)
            if operator == '-':
                sub(num1, num2)
            if operator == '/':
                quotient(num1, num2)
            if operator == '*':
                multi(num1, num2)
        except OverflowError:
            print("Sorry result is too large")
            break
calculator()