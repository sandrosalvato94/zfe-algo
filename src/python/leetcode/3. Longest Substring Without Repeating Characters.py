#Medium
#HashTable, String, Sliding Window

"""
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

    Given a string s, find the length of the longest substring without duplicate characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


    Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

"""
    Execution takes
    - 6 ms beating 99.39 % O(N)
    - 18.02 MB beating 12.13% O(1)
"""


def lengthOfLongestSubstring(self, s: str) -> int:
    lenS = len(s)

    if lenS <= 1:
        return lenS

    discover = dict()
    best = 0
    start = 0

    for index, letter in enumerate(s):
        if not letter in discover:
            discover[letter] = index
        else:
            if discover[letter] >= start:
                start = discover[letter] + 1
            discover[letter] = index

        windowSize = index - start + 1
        if windowSize > best:
            best = windowSize

    if best == 0:
        return lenS
    else:
        return best