#Easy
#Math

"""
    Given an integer x, return true if x is a palindrome, and false otherwise.

    Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.
    Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


    Constraints:

    -231 <= x <= 231 - 1


    Follow up: Could you solve it without converting the integer to a string?

"""

"""
    Execution takes 
    - 8 ms beating 52.23% O(N)
    - 18.07 MB beating 19.95 O(N)
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        if 0 <= x <= 9:
            return True

        database = dict()

        num = x
        iter = 0
        while (num > 0):
            digit = num % 10
            num //= 10
            database[iter] = digit
            iter += 1

        len_x = len(database)

        middle = (len_x // 2) - 1 * int(len_x % 2 == 0)

        """
            121     3   m=0

            1221    4   m=1

            12321   5   m=1

            123321  6   m=2
        """

        for i in range(0, middle + 1):
            """
                3 -> 0-2
                4 -> 0-3, 1-2
            """
            if database[i] != database[len_x - i - 1]:
                return False

        return True

