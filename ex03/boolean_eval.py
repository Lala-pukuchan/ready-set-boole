def eval_formula(formula: str) -> bool:
    """Evaluates a Boolean formula in Reverse Polish Notation."""
    stack = []

    for symbol in formula:
        if symbol == '0':
            stack.append(False)
        elif symbol == '1':
            stack.append(True)
        elif symbol == '!':
            if not stack:
                raise ValueError("Invalid formula: insufficient values for negation")
            operand = stack.pop()
            stack.append(not operand)
        elif symbol in '&|^>=':
            # Ensure there are at least two values for binary operations
            if len(stack) < 2:
                raise ValueError("Invalid formula: insufficient values for binary operation")
            b = stack.pop()
            a = stack.pop()

            if symbol == '&':
                stack.append(a and b)
            elif symbol == '|':
                stack.append(a or b)
            elif symbol == '^':
                stack.append(a != b)
            elif symbol == '>':
                stack.append(not a or b)  # A ⇒ B is equivalent to ¬A ∨ B
            elif symbol == '=':
                stack.append(a == b)  # A ⇔ B
        else:
            raise ValueError(f"Invalid symbol: {symbol}")

    # The result should be the only remaining value on the stack
    if len(stack) != 1:
        raise ValueError("Invalid formula: leftover values in the stack")

    return stack.pop()

# Testing the eval_formula function
if __name__ == "__main__":
    try:
        print(eval_formula("10&"))  # Output: False (0 ∧ 1)
        print(eval_formula("10|"))  # Output: True  (0 ∨ 1)
        print(eval_formula("11>"))  # Output: True  (1 ⇒ 1)
        print(eval_formula("10="))  # Output: False (1 ⇔ 0)
        print(eval_formula("101|&"))  # Output: True ((1 ∨ 0) ∧ 1)
        print(eval_formula("1!0|"))  # Output: False (0 ∨ 0)
        print(eval_formula("!"))  # Should raise ValueError
    except ValueError as e:
        print(f"Error: {e}")
