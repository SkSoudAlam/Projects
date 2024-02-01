num1 = int(input("Enter a num: "))
num2 = int(input("Enter a num: "))
operator = input('Enter a operator (+, -, /, //, *): ')
operators = ['+', '-', '/', '//', '*']
if num2 < num1:
    if operator == '+' and operator in operators:
        print(num1 + num2)

    if operator == '*' and operator in operators:
        print(num1 * num2)

    if operator == '//' and operator in operators:
        print(num1 // num2)

    if operator == '/' and operator in operators:
        print(num1 / num2)

    if operator == '-' and operator in operators:
        print(num1 - num2)

if num2 > num1:
    if operator == '+' and operator in operators:
        print(num2 + num2)

    if operator == '*' and operator in operators:
        print(num2 * num2)

    if operator == '//' and operator in operators:
        print(num2 // num2)

    if operator == '/' and operator in operators:
        print(num2 / num2)

    if operator == '-' and operator in operators:
        print(num2 - num2)


