import re


def calculate(number1: int, number2: int, operation: str) -> int:

    """Calculate result"""
    if operation == "+":
        return number1 + number2
    elif operation == "-":
        return number1 - number2
    elif operation == "*":
        return number1 * number2
    elif operation == "/":
        return number1 // number2


string = input()


regex_match = re.match(r'(-?\d+)([*/+-])(-?\d+)=(-?\d+)', string)
if regex_match:
    result = calculate(int(regex_match.group(1)),
                       int(regex_match.group(3)),
                       regex_match.group(2))
    if int(regex_match.group(4)) == result:
        print("Yes")
    else:
        print("No")
else:
    print("ERROR")
