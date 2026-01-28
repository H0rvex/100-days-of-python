logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""




def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

calculator_database = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}
def calculator():
    print(logo)
    want_to_continue = True
    first_number = float(input("Enter the first number: "))
    while want_to_continue:
        for symbol in calculator_database:
            print(symbol)
        math_operation = input("Enter the operation:")
        second_number = float(input("Enter the second number: "))
        if math_operation in calculator_database:

            if math_operation == "+" or "-" or "*" or "/":
                calculation = calculator_database[math_operation](first_number, second_number)
                print(f"{first_number} {math_operation} {second_number} = {calculation}")
                want_to_continue_ask = input("Would you like to continue? (y/n): ")
                if want_to_continue_ask == "y":
                    want_to_continue = True
                    first_number = calculation

                else:
                    want_to_continue = False
                    calculator()

        else:
            print("Invalid operation")


calculator()




