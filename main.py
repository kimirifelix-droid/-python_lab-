from utils import square, is_even, celsius_to_fahrenheit, greet


def main():
    user_input = input("Enter a number: ")
    number = float(user_input)

    print(f"Square: {square(number)}")
    print(f"Even: {is_even(number)}")
    print(f"Fahrenheit: {celsius_to_fahrenheit(number)}")
    print(greet("student"))
    print(greet("student"))


if __name__ == "__main__":
    main()
