
# main.py

import sys
from pkg.calculator import Calculator
from pkg.render import render


import io
# Force stdout to UTF-8, avoiding 'charmap' errors
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="ignore")


def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(sys.argv[1:])
    try:
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()