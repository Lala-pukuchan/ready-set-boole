from itertools import product

def eval_formula(formula: str, values: dict) -> bool:
    """Evaluates a Boolean formula in Reverse Polish Notation with variable values."""
    stack = []

    for symbol in formula:
        if symbol in values:
            stack.append(values[symbol])
        elif symbol == '0':
            stack.append(False)
        elif symbol == '1':
            stack.append(True)
        elif symbol == '!':
            if not stack:
                print("Error: insufficient values for negation")
                return None
            operand = stack.pop()
            stack.append(not operand)
        elif symbol in '&|^>=':
            if len(stack) < 2:
                print("Error: insufficient values for binary operation")
                return None
            b = stack.pop()
            a = stack.pop()

            if symbol == '&':
                stack.append(a and b)
            elif symbol == '|':
                stack.append(a or b)
            elif symbol == '^':
                stack.append(a != b)
            elif symbol == '>':
                stack.append(not a or b)
            elif symbol == '=':
                stack.append(a == b)
        else:
            print(f"Invalid symbol: {symbol}")
            return None

    if len(stack) != 1:
        print("Error: leftover values in the stack")
        return None

    return stack.pop()

def print_truth_table(formula: str):
    """Generates and prints the truth table for a given Boolean formula in RPN."""
    # Identify unique variables in the formula
    variables = sorted({symbol for symbol in formula if symbol.isalpha()})

    # Generate all possible truth value combinations for the variables
    combinations = list(product([False, True], repeat=len(variables)))

    # Print table header
    header = " | ".join(variables) + " | Result"
    print(header)
    print("-" * len(header))

    # Evaluate the formula for each combination of variable values
    for combo in combinations:
        values = dict(zip(variables, combo))
        result = eval_formula(formula, values)
        if result is None:
            print("Error encountered. Stopping further evaluation.")
            break
        row = " | ".join('1' if values[var] else '0' for var in variables) + " | " + ('1' if result else '0')
        print(row)
    print('==================')

# Testing the print_truth_table function
if __name__ == "__main__":
    print_truth_table("AB&C|")  # (A AND B) OR C
    print_truth_table("AB|C|")  # (A OR B) OR C
    print_truth_table("AB^C|")  # (A XOR B) OR C
    print_truth_table("AB>")  # (A => B)
    print_truth_table("AB=")  # (A = B)
