def int_inp(input_: any) -> float:
    try:
        return float(input_)
    except ValueError as e:
        print(f"Error: {e}")
        return int_inp(input("Again enter a number >> "))


num_one = int_inp(input("Enter a first number >> "))
num_two = int_inp(input("Enter a second number >> "))
math_operation = input("Enter operation (*, **, /, //, %, +, -) >> ")
result: float = 0

match math_operation:
    case "+": print(f"{num_one} + {num_two} = {num_one + num_two}")
    case "-": print(f"{num_one} - {num_two} = {num_one - num_two}")
    case "*": print(f"{num_one} * {num_two} = {num_one * num_two}")
    case "/": print(f"{num_one} / {num_two} = {num_one / num_two}" if num_two != 0 else "Zero division error")
    case "%": print(f"{num_one} % {num_two} = {num_one % num_two}" if num_two != 0 else "Zero division error")
    case "//": print(f"{num_one} // {num_two} = {num_one // num_two}" if num_two != 0 else "Zero division error")
    case "**": print(f"{num_one} ** {num_two} = {num_one ** num_two}")
    case _: print(f"result None. {math_operation} is not current.")

