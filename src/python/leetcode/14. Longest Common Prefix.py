#Easy
#Array String Trie

"""
    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".



    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.


    Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters if it is non-empty.

"""

"""
    Execution takes 
    - 2 ms beating 30.39% O(N * M)
    - 18.03 MB beating 50.45 O(N * M)
"""


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.nexts = dict()  # letter, Node


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        trees = dict()

        cnt_equals = 0
        curr_node = None

        best = list()
        atleast = False

        if len(strs) == 1:
            return strs[0]

        for word in strs:
            cnt_equals = 0
            word_list = list(word)
            len_word_list = len(word_list)
            i = 0

            if len_word_list > 0:
                letter = word_list[i]

                if not letter in trees:
                    if len(trees) > 0:
                        return ""
                    trees[letter] = curr_node = Node(letter)
                else:
                    curr_node = trees[letter]
                    cnt_equals += 1
            else:
                return ""

            for i in range(1, len_word_list):
                letter = word_list[i]
                if not letter in curr_node.nexts:
                    curr_node.nexts[letter] = curr_node = Node(letter)

                else:
                    curr_node = curr_node.nexts[letter]
                    cnt_equals += 1

            if len(best) == 0:
                best = list(word)
            else:
                best = best[0:cnt_equals]
                atleast = True

        if len(best) == 0 or cnt_equals == 0:
            return ""
        else:
            return ''.join(best)
