def gray_code(n: int) -> int:
    """Converts a given integer n to its Gray code equivalent."""
    return n ^ (n >> 1)

# Testing the gray_code function
if __name__ == "__main__":
    print(gray_code(0))  # Output: 0
    # | 8 | 4 | 2 | 1 |
    # |---|---|---|---|
    # | 0 | 0 | 0 | 0 | -> n
    # | 0 | 0 | 0 | 0 | -> n >> 1
    # | 0 | 0 | 0 | 0 | -> XOR
    # |---|---|---|---|
    print(gray_code(1))  # Output: 1
    # | 8 | 4 | 2 | 1 |
    # |---|---|---|---|
    # | 0 | 0 | 0 | 1 | -> n
    # | 0 | 0 | 0 | 0 | -> n >> 1
    # | 0 | 0 | 0 | 1 | -> XOR
    print(gray_code(2))  # Output: 3
    # | 8 | 4 | 2 | 1 |
    # |---|---|---|---|
    # | 0 | 0 | 1 | 0 | -> n
    # | 0 | 0 | 0 | 1 | -> n >> 1
    # | 0 | 0 | 1 | 1 | -> XOR
    # |---|---|---|---|
    print(gray_code(3))  # Output: 2
    # | 8 | 4 | 2 | 1 |
    # |---|---|---|---|
    # | 0 | 0 | 1 | 1 | -> n
    # | 0 | 0 | 0 | 1 | -> n >> 1
    # | 0 | 0 | 1 | 0 | -> XOR
    # |---|---|---|---|
    print(gray_code(4))  # Output: 6
    # | 8 | 4 | 2 | 1 |
    # |---|---|---|---|
    # | 0 | 1 | 0 | 0 | -> n
    # | 0 | 0 | 1 | 0 | -> n >> 1
    # | 0 | 1 | 1 | 0 | -> XOR
    # |---|---|---|---|
    print(gray_code(5))  # Output: 7
    print(gray_code(6))  # Output: 5
    print(gray_code(7))  # Output: 4
    print(gray_code(8))  # Output: 12

# Gray code is a binary numeral system where two successive values differ in only one bit.
# References:
    # https://qiita.com/redpeaks33/items/90ed199549be32cc4e79
