#!/usr/bin/python3
import calculator_1 as calc
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == "+":
        result = calc.add(a, b)
    elif operator == "-":
        result = calc.sub(a, b)
    elif operator == "*":
        result = calc.mul(a, b)
    elif operator == "/":
        result = calc.div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(a, operator, b, result))
