def calculation(number1, number2, calculation_type):
    result = eval(number1 + calculation_type + number2)
    return result


def main():
    allowed_calculation_types = "(+, -, *, /)"
    calculation_type = input("What kind of calculation do you want to do? " + allowed_calculation_types)
    if calculation_type == "+" or calculation_type == "-" or calculation_type == "*" or calculation_type == "/":
        print("Calculation type " + calculation_type)
        number1 = input("Please enter the first number: ")
        number2 = input("Please enter the second number: ")
        try:
            float(number1)
            float(number2)
            result = calculation(number1, number2, calculation_type)
            print(result)
        except ValueError:
            print("Error: Only numbers are allowed!")
    else:
        print("Error: Only the following types of calculation are allowed: " + allowed_calculation_types)


print("Hello and welcome to the calculator")
main()

count = 1
while count < 2:
    abort_decision = input("Do you want to continue calculating [c] or quit the program [q] ")
    if abort_decision == "c":
        main()
    elif abort_decision == "q":
        count += 1
    else:
        print("Error: You only have [c] or [q] as a choice")


print("The calculator is shutting down!")