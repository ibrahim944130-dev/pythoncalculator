import argparse

from .calculator import add, subtract, multiply, divide


def parse_args():
    parser = argparse.ArgumentParser(description="Simple calculator CLI")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Arithmetic operation")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    return parser.parse_args()


def main():
    args = parse_args()
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    result = operations[args.operation](args.a, args.b)
    print(result)


if __name__ == "__main__":
    main()
