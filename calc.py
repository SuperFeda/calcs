def int_inp(input_: any) -> float:
    try:
        return float(input_)
    except ValueError as e:
        print(f"Error: {e}")
        return int_inp(input("Again enter a number >> "))


num_one = int_inp(input("Enter a first number >> "))
num_two = int_inp(input("Enter a second number >> "))
operation = input("Enter operation (*, **, /, //, %, +, -) >> ")

match operation:
    case "+": print(f"{num_one} + {num_two} = {num_one + num_two}")
    case "-": print(f"{num_one} - {num_two} = {num_one + num_two}")
    case "*": print(f"{num_one} * {num_two} = {num_one * num_two}")
    case "/": print(f"{num_one} / {num_two} = {num_one / num_two}")
    case "%": print(f"{num_one} % {num_two} = {num_one % num_two}")
    case "//": print(f"{num_one} // {num_two} = {num_one // num_two}")
    case "**": print(f"{num_one} ** {num_two} = {num_one ** num_two}")
    case _: print(f"result None. {operation} is not current.")

