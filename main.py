def user_query(text):
    query = input(text)
    return query


def calculation(number1, number2, calculation_type):
    result = eval(number1 + calculation_type + number2)
    return result


def main():
    calculation_type = user_query("What kind of calculation do you want to do? (+, -, *, /): ")
    print("Calculation type " + calculation_type)
    number1 = user_query("Please enter the first number: ")
    number2 = user_query("Please enter the second number: ")
    print(calculation(number1, number2, calculation_type))


print("Hello and welcome to the calculator")
main()

count = 1
while count < 2:
    abort_decision = input("Do you want to continue calculating [c] or quit the program [q]? (")
    if abort_decision == "c":
        main()
    else:
        count += 1

print("The calculator is shut down!")
