def multiplier(a: int, b: int) -> int:
    result = 0  # Store the result of the multiplication

    # Loop while 'b' is greater than 0
    while b > 0:
        # If the current bit of b is 1, add 'a' to the result
        if b & 1:
            result = adder(result, a)
            print(f"Adding {a} to the result. Current result: {result}")

        # Left shift 'a' (equivalent to multiplying 'a' by 2)
        a <<= 1
        print(f"Left shifting 'a'. Current 'a': {a}")

        # Right shift 'b' (equivalent to dividing 'b' by 2)
        b >>= 1
        print(f"Right shifting 'b'. Current 'b': {b}")
        print('---')

    return result

def adder(a: int, b: int) -> int:
    """Helper function to perform addition using bitwise operations."""
    while b != 0:
        carry = a & b  # Calculate carry bits
        a = a ^ b  # Sum without carry
        b = carry << 1  # Shift carry to the left
    return a

# Testing the multiplier function
if __name__ == "__main__":
    print(multiplier(3, 4))  # Output: 12
    # | 8 | 4 | 2 | 1 |
    # |---|---|---|---|
    # | 0 | 0 | 1 | 1 | -> 3
    # | 0 | 1 | 0 | 0 | -> 4
    # |---|---|---|---|
    # shift to the left till b = 0
    print(multiplier(0, 5))  # Output: 0
    print(multiplier(7, 7))  # Output: 49
