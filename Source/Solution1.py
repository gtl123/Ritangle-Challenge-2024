"""
Solution 1 to Problem 1 in The Ritangle Challenge:

Question:
The question is split into a group of limitations.
for this question the limits are the following
1 Increasing arithmetic sequence
2 has to have 0, 9 as combined or separate digits
3 only digits 0 - 9 can be used and only once
4 All numbers are 2 digits and positive
5 There are 5 numbers in each list
"""


from itertools import permutations


def is_arithmetic_sequence(seq):
    # Check if a sequence is an arithmetic progression.
    diff = seq[1] - seq[0]

    # [(False if seq[i + 1] - seq[i] != diff else True) for i in range(1, len(seq) - 1)].count(False)
    for i in range(1, len(seq) - 1):
        if seq[i + 1] - seq[i] != diff:
            return False
    return True


def form_two_digit_numbers(perm):
    # Form five two-digit numbers from a permutation of 10 digits.
    nums = []
    for i in range(0, 10, 2):
        # Create two-digit number from adjacent digits in the permutation
        tens = perm[i]
        ones = perm[i + 1]
        num = 10 * tens + ones
        if tens == 0 and ones == 0:  # Skip invalid number 00, but allow 01 to 09
            return None
        nums.append(num)
    # print(f"DEBUG : perm is {perm} result is {nums}")
    return nums


def sum_arithmetic_sequences():
    # Sum all valid increasing arithmetic sequences formed from the digits 0 to 9.
    total_sum = 0
    invalid = 0
    non_arethmetic = 0
    digits = list(range(10))  # Digits from 0 to 9

    # Generate all permutations of the digits 0-9
    """
    PERMUTATION DEFINITION 
    The total number of permutations of (n) distinct elements (where (n) is a positive integer) is given by: [ P(n) = n! ]
    (n!) represents the factorial of (n), which is the product of all positive integers from 1 to (n).
    """
    for perm in permutations(digits):
        # Form five two-digit numbers from the permutation
        nums = form_two_digit_numbers(perm)
        if nums is None:  # Skip if invalid two-digit numbers are formed
            invalid += 1
            continue

        # Check if the numbers form an arithmetic sequence
        # all(nums[i] < nums[i + 1] for i in range(4)) checks if sequence is in ascending order
        if is_arithmetic_sequence(nums) and all(nums[i] < nums[i + 1] for i in range(4)):
            total_sum += sum(nums)
        else:
            non_arethmetic += 1

    return total_sum, invalid, non_arethmetic, len(digits)


# Run the algorithm
result, x, y, a = sum_arithmetic_sequences()
print(f"Fina Sequences {a}  with {x+y} invalid with {x} invalid due to invalid two-digit numbers and {y} invalid due bieng not arethmatic ")
print(f"Total sum of valid sequences is {result}")
