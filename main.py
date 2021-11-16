def user_query(text):
    query = input(text)
    return query


def calculation(number1, number2, calculation_type):
    result = eval(number1 + calculation_type + number2)
    return result


print("Hello and welcome to the calculator")

calculation_type = user_query("What kind of calculation do you want to do? (+, -, *, /): ")
print("Calculation type " + calculation_type)
number1 = user_query("Please enter the first number: ")
number2 = user_query("Please enter the second number: ")

print(calculation(number1, number2, calculation_type))
