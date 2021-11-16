# Functions
def calculation(number1, number2, calculation_type):
    # Performing the calculation
    result = eval(number1 + calculation_type + number2)
    # Returns the calculation
    return result


def main():
    allowed_calculation_types = "(+, -, *, /)"
    # User input which type of calculation he would like to perform
    calculation_type = input("What kind of calculation do you want to do? " + allowed_calculation_types)
    # Check whether the user input contains illegal characters
    if calculation_type == "+" or calculation_type == "-" or calculation_type == "*" or calculation_type == "/":
        # Output selected calculation type
        print("Calculation type " + calculation_type)
        # User input number 1
        number1 = input("Please enter the first number: ")
        # User input number 2
        number2 = input("Please enter the second number: ")
        # If a letter is entered for the number, the ValueError can be handled via except
        try:
            float(number1)
            float(number2)
            # Function call and store the calculation.
            result = calculation(number1, number2, calculation_type)
            # Output the result
            print(result)
        except ValueError:
            # Print output if an invalid character was entered
            print("Error: Only numbers are allowed!")
    else:
        # Print output if an invalid character was entered
        print("Error: Only the following types of calculation are allowed: " + allowed_calculation_types)


# Welcome message
print("Hello and welcome to the calculator")

# Function call
main()

# For the while loop
count = 1
# While loop to be able to call the calculator again and again
while count < 2:
    #  User input number for continue or quit
    abort_decision = input("Do you want to continue calculating [c] or quit the program [q] ")
    if abort_decision == "c":  # continue
        main()
    elif abort_decision == "q":  # quit
        count += 1
    else:
        # Print output if an invalid character was entered
        print("Error: You only have [c] or [q] as a choice")

print("The calculator is shutting down!")
