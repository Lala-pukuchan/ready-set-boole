from typing import List, Set


def eval_set(formula: str, sets: List[Set[int]]) -> Set[int]:
    """
    Evaluate the formula in RPN with the given list of sets.
    """
    stack = []
    encompassing_set = set.union(*sets) if sets else set()

    for symbol in formula:
        if "A" <= symbol <= "Z":  # Variables A-Z map to sets
            # [A, B, C, ...] -> [0, 1, 2, ...]
            index = ord(symbol) - ord("A")
            if index < len(sets):
                stack.append(sets[index])
            else:
                raise ValueError(f"Set for variable '{symbol}' not provided.")
        elif symbol == "!":  # Complement
            if not stack:
                raise ValueError("Invalid formula: missing operand for '!'")
            set_to_complement = stack.pop()
            stack.append(encompassing_set - set_to_complement)
        elif symbol == "&":  # Intersection
            if len(stack) < 2:
                raise ValueError("Invalid formula: missing operands for '&'")
            b = stack.pop()
            a = stack.pop()
            stack.append(a & b)
        elif symbol == "|":  # Union
            if len(stack) < 2:
                raise ValueError("Invalid formula: missing operands for '|'")
            b = stack.pop()
            a = stack.pop()
            stack.append(a | b)
        else:
            raise ValueError(f"Invalid symbol '{symbol}' in formula.")

    if len(stack) != 1:
        raise ValueError("Invalid formula: too many operands.")
    result = stack.pop()
    return list(result) if result else []


# Example usage
if __name__ == "__main__":
    sets = [{0, 1, 2}, {0, 3, 4}]
    print("Result for AB&:", eval_set("AB&", sets))  # Expected output: {0}

    sets = [{0, 1, 2}, {3, 4, 5}]
    print(
        "Result for AB|:", eval_set("AB|", sets)
    )  # Expected output: {0, 1, 2, 3, 4, 5}

    sets = [{0, 1, 2}]
    print("Result for A!:", eval_set("A!", sets))  # Expected output: set()

    sets = [{0, 1, 2}, {0, 3, 4}, {3, 4, 5}]
    print("Result for AB|C&:", eval_set("AB|C&", sets))  # Expected output: {0}
