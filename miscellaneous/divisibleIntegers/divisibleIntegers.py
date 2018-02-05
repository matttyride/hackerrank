#!usr/bin/env python

"""
Given an array of integers, find whether it’s possible to construct an integer
using all the digits of the numbers in the array such that it would be
divisible by n (where n is 1 <= n <= 9).
If it's possible, return true, else return false.

Examples:
    divisibleIntegers(n = 3, arr= [40, 50, 90])
    > true // 945000 is divisible by 3

Read about divisibility rules on wikipedia.
"""

from itertools import combinations, permutations

def divisibleIntegers(n, arr):
    print(n, arr)
    # Check for single integer arrays
    if len(arr) == 1:
        if arr[0] % n == 0:
            return True
        else:
            return False
    # Process array
    str_arr = [list(str(i)) for i in arr]
    digits = []
    for i in str_arr:
        digits = digits + i
    # Divisibility cases
    if n == 1:
        return True
    # Rule: The last digit is even (0, 2, 4, 6, or 8).
    if n == 2:
        if any(int(i) % 2 == 0 for i in digits):
            return True
        return False
    # Rule: Sum the digits. The result must be divisible by 3/9.
    if n == 3 or n == 9:
        if sum([int(i) for i in digits]) % n == 0:
            return True
        return False
    # Rule: Twice the tens digit, plus the ones digit is divisible by 4.
    if n == 4:
        for perm in permutations(digits, 2):
            four_rule = 2 * int(perm[0]) + int(perm[1])
            if four_rule % 4 == 0:
                return True
        return False
    # Rule: The last digit is 0 or 5.
    if n == 5:
        if any(int(i) == 5 or int(i) == 0 for i in digits):
            return True
        return False
    # Rule: It is divisible by 2 and by 3.
    if n == 6:
        if any(int(i) % 2 == 0 for i in digits):
            if sum([int(i) for i in digits]) % 3 == 0:
                return True
        return False
    # Rule: Adding the last digit to 3 times the rest gives a multiple of 7.
    if n == 7:
        for perm in permutations(digits, len(digits)):
            seven_rule = int(perm[0]) + (3 * int(''.join(perm[1:])))
            if seven_rule % 7 == 0:
                return True
        return False
    # Rule: Add the last digit to twice the rest.
    # The result must be divisible by 8.
    if n == 8:
        for perm in permutations(digits, len(digits)):
            eight_rule = int(perm[0]) + (2 * int(''.join(perm[1:])))
            if eight_rule % 8 == 0:
                return True
        return False

def test_cases():
    print(divisibleIntegers(n = 1, arr = [1, 1, 1]), True)
    print(divisibleIntegers(n = 2, arr = [1]), False)
    print(divisibleIntegers(n = 2, arr = [2]), True)
    print(divisibleIntegers(n = 2, arr = [1, 1, 1]), False)
    print(divisibleIntegers(n = 2, arr = [40, 50, 90]), True)
    print(divisibleIntegers(n = 3, arr = [40, 50, 90]), True)
    print(divisibleIntegers(n = 3, arr = [50, 50, 90]), False)
    print(divisibleIntegers(n = 4, arr = [32, 50, 90]), True)
    print(divisibleIntegers(n = 4, arr = [2, 5]), True)
    print(divisibleIntegers(n = 4, arr = [35, 9, 2]), True)
    print(divisibleIntegers(n = 4, arr = [3, 5, 9]), False)
    print(divisibleIntegers(n = 5, arr = [40, 50, 90]), True)
    print(divisibleIntegers(n = 5, arr = [41, 63, 92]), False)
    print(divisibleIntegers(n = 5, arr = [41, 51, 91]), True)
    print(divisibleIntegers(n = 7, arr = [48, 35, 95]), True)
    print(divisibleIntegers(n = 7, arr = [2, 2, 5]), True)
    print(divisibleIntegers(n = 7, arr = [4, 5, 2]), True)
    print(divisibleIntegers(n = 7, arr = [5, 0]), False)
    print(divisibleIntegers(n = 8, arr = [6, 5]), True)
    print(divisibleIntegers(n = 8, arr = [3, 4, 5, 2, 1]), True)
    print(divisibleIntegers(n = 8, arr = [3, 5, 2]), True)
    print(divisibleIntegers(n = 8, arr = [4, 1]), False)
    print(divisibleIntegers(n = 9, arr = [8, 1]), True)
    print(divisibleIntegers(n = 9, arr = [1, 5]), False)
    print(divisibleIntegers(n = 9, arr = [4, 5]), True)

if __name__ == '__main__':
    test_cases()
