#Medium
#String

#Note: I didn't resolve it

"""
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);


    Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
    Example 2:

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    Example 3:

    Input: s = "A", numRows = 1
    Output: "A"


    Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000

"""


class VStructure(object):
    def __init__(self, n_rows, offset=0):
        self.offset = offset

        self.n_rows = n_rows  # 4
        self.n_cols = n_rows - 1  # 3

        self._curr_i = 0  # i_offset
        self._curr_j = 0  # j_offset

        self.size = n_rows * 2 - 2
        self._curr_size = 0

        self._letters = [" "] * self.size

    def push(self, letter):

        if self._curr_size < self.n_rows:
            self._letters[self._curr_i] = letter
            self._curr_size += 1
            # index = self._curr_i
            self._curr_i = (self._curr_i + 1) * self.n_cols
        else:
            """
                r = 4, c = 3, i = 9, i* = 7
                r = 4, c = 3, i = 7, i* = 5
            """
            self._curr_i = self._curr_i - self.n_cols - 1
            self._letters[self._curr_i] = letter
            self._curr_size += 1

    def isThereSpaceAvailable(self):
        return self._curr_size < self.size


class ZZRow(object):
    def __init__(self, n):
        self._row = list()
        self._n_colm = n


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        lenS = len(s)
        columnStep = numRows - 2  # cs = 1 -> nr = 3, cs = 2 -> nr = 4, cs = 3 -> nr = 5
        sizeVStructure = numRows + columnStep

        totVCompleteStructure = lenS // (sizeVStructure)
        # remainingCharacters = lenS - totVCompleteStructure

        solution = [" "]
        head = 0

        v = VStructure(numRows)
        id_structure = 0

        zz = dict(
            id_structure: VStructure(numRows)
        )

        for i in range(lenS):
            if zz[id_structure].isThereSpaceAvailable():
                zz[id_structure].push(s[i])
            else:
                # submit previous v

                id_structure += 1

                """
                    id = 0, j = 0, cs = 2
                    id = 1, j = 3, cs = 2
                    id = 2, j = 6, cs = 2
                """

                zz[id_structure] = VStructure(numRows, offset=id_structure * (columnStep + 1))
                zz[id_structure].push(s[i])

        for i in range(lenS):
            for id, v in zz.items():
                solution.append

        solution = "".join(solution)
        return solution
