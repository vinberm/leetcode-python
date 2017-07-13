"""
created by Nov
2017-7-13
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def addTwoNumber(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        """
        # point to the same list
        result = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            # 每相应节点相加，if sum > 10, then 后面节点相加结果再加1
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return result.next



def main():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)

    l2 = ListNode(2)
    l2.next = ListNode(8)
    l2.next.next = ListNode(7)

    solu = Solution()
    result = solu.addTwoNumber(l1, l2)
    while(result):
        print(result.val, end='->')
        result = result.next

if __name__ == '__main__':
    main()
