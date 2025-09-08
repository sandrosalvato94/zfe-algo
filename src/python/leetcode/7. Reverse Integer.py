#Medium
#Math

"""
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



    Example 1:

    Input: x = 123
    Output: 321
    Example 2:

    Input: x = -123
    Output: -321
    Example 3:

    Input: x = 120
    Output: 21

"""

"""
    Execution takes
    - 50ms beating 7.15% O(N)
    - 17.68 beating 83.42 % O(N)
"""

"""
    ChatGpt solution

    class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        res = 0
        n = abs(x)

        while n != 0:
            digit = n % 10
            n //= 10

            # controllo overflow PRIMA di moltiplicare
            # controlla questo res * 10 + digit <= INT_MAX
            # ma non fa la moltiplicazione prima ma piuttosto la divisone
            if res > (INT_MAX - digit) // 10:
                return 0

            res = res * 10 + digit

        return res if x >= 0 else -res

"""


class Solution:
    def reverse(self, x: int) -> int:

        minThr = -2 ** 31
        maxThr = 2 ** (31) - 1

        if x < 0:
            mult = -1
        else:
            mult = 1

        numStr = list(str(abs(x)))
        n_digits = len(numStr)

        j = 0

        """
            123456 3, 6

            12345, 3, 5

            1234 , middle = 2, len = 4

            120 , middle = 2, len = 3

            12,   middle = 1, len = 2
        """

        middle = (n_digits // 2) + 1 * (n_digits % 2 != 0)

        isLastZero = True

        for i in range(n_digits - 1, middle - 1, -1):
            numStr[j], numStr[i] = numStr[i], numStr[j]
            j += 1

        rv = 0
        for i in range(0, n_digits):

            digit = int(numStr[i])
            if rv + digit == 0:
                continue

            rv = rv * 10 + digit
            if not (minThr <= rv <= maxThr):
                return 0

        return rv * mult