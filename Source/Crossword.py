"""
    # PUZZLE P
s.is_prime_multiple(s.gv("1dn"),s.gv("4dn")),
s.is_square(s.digit_sum(s.gv("2dn"))),
s.is_square(s.gv("1ac")),
s.is_prime(int(str(s.gv("3ac"))[::-1])),

# PUZZLE Q

s.gv("1dn") == "WHAT IS DIGITIAL SUM SQUARED ?" + int(str(s.gv("3ac"))[::-1]),
s.is_palindromic_prime(s.gv("1ac")),
s.is_cube(s.gv("4dn")),
s.gv("1dn") == s.gv("1ac") - s.digit_sum(s.gv("1dn")),
s.is_prime(s.gv("2dn")),
# PUZZLE R

s.gv("2dn") == s.digit_product(s.gv("1ac")) +  s.digit_product(s.gv("1dn")),
s.gv("1dn") == s.digit_sum(s.gv("2dn")),
s.gv("4dn") == s.gv("5ac") - "SQUARE OF WHATT?",
s.gv("3ac") == s.gv("4dn") - s.digit_sum(s.gv("4dn")),

# PUZZLE S
s.gv("1dn") == (s.digit_sum(s.gv("1ac"))**2) + s.gv("3ac"),
s.is_triangular(s.gv("4dn")),
False if False in [s.gv("3ac") == s.triangular(n) - s.gv("4dn") for n in range(100)] else True,
s.gv("2dn") == int(str(s.gv("3ac"))[::-1]),
"""

import math

class Crossword:

    def __init__(s):
        s.template = [["1", "2", " "],
                      [" ","3","4"],
                      ["5"," "," "], ]
        s.Crossword =[[1, 0, 0],
                      [5,0,5],
                      [3,0,0], ]
        is_prime = lambda n: (False if (n <= 1) else False if False in [(False if (n % i == 0) else True) for i in range(2, int(n ** 0.5) + 1)] else True)
        s.is_palindrome = lambda n: str(n) == str(n)[::-1]
        s.is_prime = lambda n:(False if (n <= 1) else False if False in [(False if (n % i == 0) else True) for i in range(2, int(n ** 0.5) + 1)] else True)
        s.is_square = lambda n: int(math.sqrt(n)) * int(math.sqrt(n)) == n
        s.gv = lambda v:(int("".join([str(s.Crossword[n][s.find_index(v[0], s.template)[1]]) for n in range(s.find_index(v[0], s.template)[0], 3)])) if v[1:] == "dn" else int("".join([str(s.Crossword[s.find_index(v[0], s.template)[0]][n]) for n in range(s.find_index(v[0], s.template)[1], 3)])))
        s.digit_sum = lambda n:0 if n == 0 else (1 + (n - 1) % 9)
        s.is_prime_multiple = lambda A,B: False if (B == 0 or A % B != 0) else is_prime(( A // B))
        s.is_cube = lambda n: int(math.cbrt(n)) **3 == n
        s.triangular  = lambda n: n(n+1)/2
        s.is_triangular = lambda num: False if (num < 0 or (1 + 8 * num  ) < 0) else ((-1 + math.sqrt((1 + 8 * num))) / 2).is_integer()
        s.pprimes  = [101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919, 929]


    def Try_Insert(s,value,place):
        pass

    def number_to_crossword(s,number):
            """
            Convert a 9-digit number into a 3x3 crossword grid.
            Zeros in the number are represented as empty cells in the crossword.
            """
            digits = [int(digit) for digit in str(number)]
            crossword = [digits[i:i + 3] for i in range(0, 9, 3)]
            return crossword


    def check(s):
        check = [
            # PUZZLE P
            s.is_prime_multiple(s.gv("1dn"), s.gv("4dn")),
            s.is_square(s.digit_sum(s.gv("2dn"))),
            s.is_square(s.gv("1ac")),
            s.is_prime(int(str(s.gv("3ac"))[::-1])),
        ]
        return  False if False in check else True


    def find_index(s,item, lst):
        for i, row in enumerate(lst):
            if item in row:
                return ( i, row.index(item) )
        return None

    def is_palindromic_prime(s,n):
        "Check if a number is a palindromic prime."
        return s.is_prime(n) and s.is_palindrome(n)

    def digit_product(s,n):
        digits = [int(digit) for digit in str(n)]  # Convert the number into a list of digits
        digit_sum = sum(digits)  # Sum of the digits
        digit_product = 1
        for digit in digits:  # Product of the digits
            digit_product *= digit
        return digit_sum * digit_product  # Multiply sum and product of the digits


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_combinations():
    combinations = []
    for three_digit in range(100, 1000):
        for two_digit in range(10, 100):
            if two_digit != 0 and three_digit % two_digit == 0:
                quotient = three_digit // two_digit
                if is_prime(quotient):
                    combinations.append((three_digit, two_digit, quotient))
    return combinations

combinations = find_combinations()
for combo in combinations:
    print(f"{combo[0]} is a multiple of {combo[1]} and the quotient {combo[2]} is a prime number")


