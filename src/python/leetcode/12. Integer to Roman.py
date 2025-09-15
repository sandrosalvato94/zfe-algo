#Medium
#Hash Table Math String

"""
    Seven different symbols represent Roman numerals with the following values:

    Symbol	Value
    I	1
    V	5
    X	10
    L	50
    C	100
    D	500
    M	1000
    Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

    If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
    If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
    Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
    Given an integer, convert it to a Roman numeral.



    Example 1:

    Input: num = 3749

    Output: "MMMDCCXLIX"

    Explanation:

    3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
     700 = DCC as 500 (D) + 100 (C) + 100 (C)
      40 = XL as 10 (X) less of 50 (L)
       9 = IX as 1 (I) less of 10 (X)
    Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
    Example 2:

    Input: num = 58

    Output: "LVIII"

    Explanation:

    50 = L
     8 = VIII
    Example 3:

    Input: num = 1994

    Output: "MCMXCIV"

    Explanation:

    1000 = M
     900 = CM
      90 = XC
       4 = IV


    Constraints:

    1 <= num <= 3999

"""

"""
    Execution takes 
    - 16 ms beating 5.38% O(N)
    - 18.02 MB beating 5.91 O(1)
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        ht = {
            1000: ('M', 3),
            500: ('D', 1),
            100: ('C', 3),
            50: ('L', 1),
            10: ('X', 3),
            5: ('V', 1),
            1: ('I', 3)
        }

        rv = list()
        i = 0
        num_str = list(str(num))
        len_original = len_num = prev_len = len(num_str)

        for R in ht:

            if prev_len != len_num:
                i += 1
            if i >= len_original:
                break

            prev_len = len_num

            if not num_str[0] in ['4', '9']:
                cnt = 0
                while cnt < ht[R][1]:
                    if num - R >= 0:
                        rv.append(ht[R][0])
                        cnt += 1
                        num -= R
                    else:
                        break
            else:
                prev = 1000
                next = 1
                for R_star in ht:
                    if R_star - num > 0:
                        prev = R_star
                    else:
                        if num // R_star == 4:
                            rv = rv + [ht[R_star][0], ht[prev][0]]
                            break
                        else:
                            if next == 0:
                                rv = rv + [ht[R_star][0], ht[prev][0]]
                                break
                            else:
                                next -= 1

                num_str.pop(0)
                try:
                    num = int(''.join(num_str))
                except:
                    num = 0

            num_str = list(str(num))
            len_num = len(num_str)

        return ''.join(rv)