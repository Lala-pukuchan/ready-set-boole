from typing import List


def powerset(input_set: List[int]) -> List[List[int]]:
    """
    Generate the powerset of a given set of integers.
    Find all possible subsets of the input set.
    complexity: O(2^n)
    """
    n = len(input_set)
    power_set = []

    # There are 2^n subsets for a set with n elements
    for i in range(2**n):
        subset = []
        for j in range(n):
            # Check if the j-th element is included in the i-th subset
            # if i = 5, j = 2
            # 5 = 101 & 100 = 100
            # include the 3rd element in the subset
            if (i & (1 << j)) != 0:
                subset.append(input_set[j])
        power_set.append(subset)

    return power_set


# Example usage
if __name__ == "__main__":
    example_set = [1, 2, 3]
    print("Power set:", powerset(example_set))

    example_set = [1, 2, 3, 4]
    print("Power set:", powerset(example_set))
