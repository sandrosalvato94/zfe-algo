#Medium
#LinkedList, Math, Recursion (?)

"""
    https://leetcode.com/problems/add-two-numbers/description/

    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
    Example 2:

    Input: l1 = [0], l2 = [0]
    Output: [0]
    Example 3:

    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

    Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""

"""
    Execution takes
    - 218 ms beating 5.37% O(Max(N,M))
    - 18.82 MB beating 14.38 % O(Max(N,M))

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from concurrent.futures import ThreadPoolExecutor

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def _convertToInt(l: Optional[ListNode]):
        currNode = l

        rv = currNode.val
        iThDigit = 1

        while not currNode.next is None:
            currNode = currNode.next
            rv += (currNode.val * (10 ** iThDigit))
            iThDigit += 1

        return rv

    def _convertToList(num: int):
        rv = list()
        numList = list(str(num))
        lenList = len(numList)

        headList = ListNode(val=int(numList[lenList - 1]), next=None)
        pNode = headList

        for i in range(lenList - 2, -1, -1):
            # rv.append(int(numList[i]))
            pNode.next = ListNode(val=int(numList[i]), next=None)
            pNode = pNode.next

        return headList

    with ThreadPoolExecutor(max_workers=2) as ex:
        f1 = ex.submit(_convertToInt, l1)
        f2 = ex.submit(_convertToInt, l2)

        num1 = f1.result()
        num2 = f2.result()

    result = num1 + num2
    return _convertToList(result)