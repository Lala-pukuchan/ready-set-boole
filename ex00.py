def adder(a: int, b: int) -> int:
    while b != 0:
        # Calculate the carry bits
        carry = a & b

        # Sum without the carry
        a = a ^ b

        # Shift carry bits to the left
        b = carry << 1

    return a


# Testing the adder function
if __name__ == "__main__":
    print(adder(5, 3))
    print(adder(0, 0))
    print(adder(15, 10))
