#Mediaum
#TwoPointers, String, DynamicProgramming

"""
    Given a string s, return the longest palindromic substring in s.



    Example 1:

    Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.
    Example 2:

    Input: s = "cbbd"
    Output: "bb"


    Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""

"""
    Execution takes 
    - 1870 ms beating 27.73%
    - 18.12 MB beating 18.30%
    
"""

import copy


class Solution:
    def longestPalindrome(self, s: str) -> str:

        def _buildEncoder(s: str) -> dict:
            encoder = dict()
            for index, letter in enumerate(s):
                if not letter in encoder:
                    encoder[letter] = list()
                encoder[letter].append(index)

            return encoder

        def _findSolution(s: str, encoder: dict):

            targetLen = 0
            targetSubs = ""

            def _checkPalindromic(subs: str, lenSubs: int) -> bool:

                if lenSubs <= 3:
                    return True

                start = 1
                end = lenSubs - 2  # is an index, moreover i m not interested in the last c
                middleFromLeft = ((lenSubs // 2) - 1 * int((lenSubs % 2 == 0)))

                """
                    anna, lenSubs = 4, lenSybs // 2 = 2
                    start = 1
                    end = 2
                    middle = 1
                """

                """
                    abbba, lenSubs = 5, lenSubs // 2 = 2
                    start = 1
                    end = 3,
                    middle = 2
                """

                """
                    abcddcba, lenSubs = 8, lenSubs // 2 = 4
                    start = 1
                    end = 6,
                    middle = 3
                """

                """
                    barrab, lenSubs = 6, lenSubs // 2 = 3
                    start = 1
                    end = 4
                    middle = 2
                """

                while (start <= middleFromLeft):
                    if subs[start] != subs[end]:
                        return False
                    start += 1
                    end -= 1

                return True

            for letter, occurencies in encoder.items():
                howManyOccurencies = len(occurencies)
                """
                    barrabba
                    encoder:
                        b: [0, 5, 6]
                        a: [1, 4, 7]
                        r: [2, 3]

                    anna
                    encoder:
                        a: [0, 3]
                        n: [1, 2]
                """
                if howManyOccurencies > 2:
                    for l in range(howManyOccurencies):
                        for r in range(howManyOccurencies - 1, l, -1):
                            start, end = occurencies[l], occurencies[r]
                            lenSubs = end - start + 1

                            if lenSubs < targetLen:
                                break

                            subs = s[start:end + 1]

                            isPalindromic = _checkPalindromic(
                                subs,
                                lenSubs
                            )

                            if isPalindromic and lenSubs > targetLen:  # short-circuit evaluation
                                targetSubs = copy.copy(subs)
                                targetLen = lenSubs

                elif howManyOccurencies == 2:
                    start, end = occurencies[0], occurencies[1]
                    lenSubs = end - start + 1

                    if lenSubs < targetLen:
                        break

                    subs = s[start:end + 1]

                    isPalindromic = _checkPalindromic(
                        subs,
                        lenSubs
                    )

                    if isPalindromic and lenSubs > targetLen:  # short-circuit evaluation
                        targetSubs = copy.copy(subs)
                        targetLen = lenSubs

                else:
                    pass

            return targetSubs

        if len(s) == 1:
            return s[0]

        encoder = _buildEncoder(s)

        rv = _findSolution(s, encoder)

        return rv if rv != "" else s[0]
