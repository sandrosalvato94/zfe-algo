#Medium
#String

"""
    Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

    The algorithm for myAtoi(string s) is as follows:

    Whitespace: Ignore any leading whitespace (" ").
    Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
    Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
    Return the integer as the final result.



    Example 1:

    Input: s = "42"

    Output: 42

    Explanation:

    The underlined characters are what is read in and the caret is the current reader position.
    Step 1: "42" (no characters read because there is no leading whitespace)
             ^
    Step 2: "42" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "42" ("42" is read in)
               ^
    Example 2:

    Input: s = " -042"

    Output: -42

    Explanation:

    Step 1: "   -042" (leading whitespace is read and ignored)
                ^
    Step 2: "   -042" ('-' is read, so the result should be negative)
                 ^
    Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
                   ^
    Example 3:

    Input: s = "1337c0d3"

    Output: 1337

    Explanation:

    Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
             ^
    Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
                 ^
    Example 4:

    Input: s = "0-1"

    Output: 0

    Explanation:

    Step 1: "0-1" (no characters read because there is no leading whitespace)
             ^
    Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
             ^
    Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
              ^
    Example 5:

    Input: s = "words and 987"

    Output: 0

    Explanation:

    Reading stops at the first non-digit character 'w'.



    Constraints:

    0 <= s.length <= 200
    s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

"""

"""
    Execution takes
    - 2 ms beating 45.58 % O(N)
    - 17.93 MB beating 29.59 % O(1)
"""

"""
    Note ChatGpt

    🔧 Micro-migliorie

    Regex più snella (ed esplicita con raw string)

    Con re.match l’ancora ^ è implicita, ma usare r"..." evita backslash ambigui.

    Il pezzo finale \D*\d* non ti serve: leggi solo il prefisso valido.

    my_regex = re.compile(r"\s*([\-+]?)0*(\d+)")


    Nomi e costanti

    POW31 è ok; volendo rendi espliciti i limiti:

    INT_MIN, INT_MAX = -2**31, 2**31 - 1


    Poi usa bound = INT_MAX if mult==1 else -INT_MIN per leggibilità.

    Righe inutili

    isLastZero non usata → toglila.

    Il commento “# if rv*10 + digit < HIGH_BOUND ...” è utile; puoi lasciarlo, ma allinea la notazione (HIGH_BOUND → INT_MAX).

    Leggibilità del check overflow

    La tua formula è corretta. Se vuoi chiarirla:

    # bound magnitudine: 2147483647 per +, 2147483648 per -
    limit = (2**31 - 1) if mult == 1 else 2**31
    if rv > (limit - digit) // 10:
        return INT_MAX if mult == 1 else INT_MIN

"""

import re

class Solution:
    def myAtoi(self, s: str) -> int:

        POW31 = 2 ** 31

        my_regex = re.compile("\s*([\-+]?)0*(\d+)\D*\d*")
        rv = my_regex.match(s)

        if not rv is None:
            sign,char2process = rv.groups()[0], rv.groups()[1]
        else:
            return 0

        if sign == "-":
            mult = -1
        else:
            mult = +1

        rv = 0

        for digit in char2process:
            #rv = rv*10 + digit
            # if rv*10 + digit < HIGH_BOUND --> rv*10 < HIGH_BOUND - digit --> rv < (HIGH_BOUND - digit) // 10
            # if rv*
            digit = int(digit)
            if rv <= (POW31 -1*(int(mult == 1)) - digit) // 10:
                rv = rv*10 + digit
            else:
                return mult*(POW31 -1*(int(mult == 1)))

        return rv*mult