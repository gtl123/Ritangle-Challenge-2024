"""
@GAURAV SHUKLA
Code Notes:
Solution 1 to Problem 1 in The Ritangle Challenge:

Question:
The question is split into a group of limitations.
for this question the limits are the following
1 Increasing arithmetic sequence
2 has to have 0, 9 as combined or separate digits
3 only digits 0 - 9 can be used and only once
4 All numbers are 2 digits and positive
5 There are 5 numbers in each list

THIS CODE IS PURPOSELY NOT EFFICIENT RATHER IT IS VERY COMPACT AND PRIORITISES THE LEAST LINES

    PERMUTATION DEFINITION
    The total number of permutations of (n) distinct elements (where (n) is a positive integer) is given by: [ P(n) = n! ]
    (n!) represents the factorial of (n), which is the product of all positive integers from 1 to (n).

"""
from itertools import permutations
is_arithmetic_sequence = lambda seq: False if( False in [(False if seq[i + 1] - seq[i] != (seq[1] - seq[0]) else True) for i in range(1, len(seq) - 1)]) else True
def form_two_digit_numbers(perm):
    nums = []
    [None if (perm[i] == 0 and perm[i + 1] == 0) else nums.append(10 * perm[i] + perm[i + 1]) for i in range(0, 10, 2)]
    return  nums
def sum_arithmetic_sequences():
    total_sum = 0
    for perm in permutations(list(range(10))):
        nums = form_two_digit_numbers(perm)
        if nums is None:continue
        total_sum += (sum(nums) if is_arithmetic_sequence(nums) and all(nums[i] < nums[i + 1] for i in range(4)) else 0)
    return total_sum
result = sum_arithmetic_sequences()
print(f"Total sum of valid sequences is {result}")