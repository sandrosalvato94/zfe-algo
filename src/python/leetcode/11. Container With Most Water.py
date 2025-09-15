#Medium
#Array Two Pointers Greedy

"""
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.



    Example 1:


    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
    Example 2:

    Input: height = [1,1]
    Output: 1


    Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104

"""

"""
    Execution takes 
    - 107 ms beating 38.18% O(N)
    - 128.69 MB beating 23.89 O(1)
"""


class Solution:

    def maxArea(self, height: List[int]) -> int:

        L, R = 0, len(height) - 1
        best = 0

        while L < R:
            h = min(height[L], height[R])
            width = R - L
            best = max(best, h * width)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return best

    """
        Exceeds time

        def maxArea(self, height: List[int]) -> int:
            ix = 0
            target = 0
            n_elements = len(height)

            if n_elements == 2:
                return min(height[0], height[1])

            for left in range(0, n_elements-1):
                h_left = height[left]
                for right in range(left+1, n_elements):
                    h_right = height[right]

                    if min(h_left, h_right) * (right - left) > target:
                        target = min(h_left, h_right) * (right - left)

            return target
    """