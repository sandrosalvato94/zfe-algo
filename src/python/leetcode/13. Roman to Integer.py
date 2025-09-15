#Easy
#Hash Table Math String

"""
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.



    Example 1:

    Input: s = "III"
    Output: 3
    Explanation: III = 3.
    Example 2:

    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
    Example 3:

    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


    Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].

"""

"""
    Execution takes 
    - 8 ms beating 26.29% O(N)
    - 17.76 MB beating 64.34 O(1)
"""


class Solution:
    def romanToInt(self, s: str) -> int:

        ht = {
            'I': (1, 3),
            'IV': (4, 1),
            'V': (5, 1),
            'IX': (9, 1),
            'X': (10, 3),
            'XL': (40, 1),
            'L': (50, 1),
            'XC': (90, 1),
            'C': (100, 3),
            'CD': (400, 1),
            'D': (500, 1),
            'CM': (900, 1),
            'M': (1000, 3)
        }

        string = list(s)
        i = len_string = len(string)

        buffer = []
        rv = 0

        i -= 1

        while (i >= 0):
            letter = string[i]
            num, rep = ht[letter][0], ht[letter][1]

            if i - 1 >= 0:
                letter_next = string[i - 1]
                buffer += [letter_next, letter]
                buffer_str = ''.join(buffer)

                if buffer_str in ht:
                    rv += ht[buffer_str][0]
                    i -= 1
                else:
                    rv += ht[letter][0]

                buffer = []
            else:
                rv += ht[letter][0]

            i -= 1

        return rv



