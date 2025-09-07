"""
    https://leetcode.com/problems/median-of-two-sorted-arrays/description/

    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).



    Example 1:

    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
    Example 2:

    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


    Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

"""

"""
    Execution takes
    - 4 ms beating 33.85% O(M+N)
    - 18.30 MB beating 19.47 % O(1)
"""


def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def _extractMedianFromList(l: List[int], s: int):
        if ((s % 2) == 0):  # is Even True
            return float((l[s // 2] + l[(s // 2) - 1]) / 2)
        else:  # is Odd
            return float(l[(s - 1) // 2])

    len1 = len(nums1)
    len2 = len(nums2)
    lenTotal = len1 + len2

    if ((lenTotal % 2) == 0):  # is Even True
        iMedianL, iMedianR = ((lenTotal // 2) - 1), (lenTotal // 2)
    else:
        iMedianL, iMedianR = ((lenTotal - 1) // 2), ((lenTotal - 1) // 2)

    if len1 > 0 and len2 > 0:
        i1 = 0
        i2 = 0
        iTotal = 0
        mL, mR = None, None

        INF = float('inf')
        while (iTotal <= iMedianR) and (i1 < len1 or i2 < len2):
            next1 = nums1[i1] if i1 < len1 else INF
            next2 = nums2[i2] if i2 < len2 else INF

            if next1 <= next2:
                curr = next1
                i1 += 1
            else:
                curr = next2
                i2 += 1

            if iTotal == iMedianL:
                mL = curr
            if iTotal == iMedianR:
                mR = curr
                break

            iTotal += 1

        if ((lenTotal % 2) == 0):  # is Even True
            return float((mL + mR) / 2)
        else:  # is Odd
            return float(mR)

    elif len1 > 0 and len2 == 0:
        return _extractMedianFromList(nums1, len1)
    elif len1 == 0 and len2 > 0:
        return _extractMedianFromList(nums2, len2)
    else:
        return None