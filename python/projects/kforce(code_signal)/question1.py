"""
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a
number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and
return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
solution(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
solution(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer a

The first number, without its leading zeros.

Guaranteed constraints:
0 ≤ a size ≤ 104,
0 ≤ element value ≤ 9999.

[input] linkedlist.integer b

The second number, without its leading zeros.

Guaranteed constraints:
0 ≤ b size ≤ 104,
0 ≤ element value ≤ 9999.

[output] linkedlist.integer

The result of adding a and b together, returned without leading zeros in the same format.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

"""
from typing import Optional


#
# # def solution(a, b):
# #     # print(a, b)
# #     # s = sum(a) + sum(b)
# #     # print(s)
# #     x = ''.join(a)
# #     y = ''.join(b)
# #
# #     # [''.join(item) for item in zip(*[iter(s)] * 4)]
# #     # return map(int, str(x))
# #
# # solution([9876, 5432, 1999], [1, 8001])
#
# # def merge_lists(h1, h2):
# #     if h1 is None:
# #         return h2
# #     if h2 is None:
# #         return h1
# #
# #     if (h1 < h2):
# #         h1 = merge_lists(h1, h2)
# #         return h1
# #     else:
# #         h2 = merge_lists(h2, h1)
# #         return h2
# #
# #
# # merge_lists([9876, 5432, 1999], [1, 8001])
#
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None


#
# def solution(l1, l2):
#     temp = ListNode(None)
#
#     l1 = ListNode(l1)
#     l2 = ListNode(l2)
#
#     print(l1)
#     print(l2)
#     if l1 is None:
#         return l2
#     if l2 is None:
#         return l1
#     if l1.value <= l2.value:
#         temp = l1
#         temp.next = solution(l1.next, l2)
#     else:
#         temp = l2
#         temp.next = solution(l1, l2.next)
#     return temp
#
#
# def addTwoHugeNumbers(a, b):
#     new_a = reverse_linked_list(a)
#     new_b = reverse_linked_list(b)
#     curr_a, curr_b = new_a, new_b
#     carry = 0
#     new_head = None
#     prev = None
#     while curr_a is not None or curr_b is not None:
#         curr, carry = add_list_elem(curr_a, curr_b, carry)
#         if prev:
#             prev.next = curr
#             prev = curr
#         if new_head is None:
#             new_head = curr
#             prev = curr
#         if curr_a:
#             curr_a = curr_a.next
#         if curr_b:
#             curr_b = curr_b.next
#     if carry:
#         curr = ListNode(carry)
#         prev.next = curr
#     new_head = reverse_linked_list(new_head)
#     # reverse the inputed lists back, try to avoid side effects
#     reverse_linked_list(new_a)
#     reverse_linked_list(new_b)
#     return new_head
#
#
# def reverse_linked_list(head):
#     """reverse linked list, tail becomes head and new head is returned
#     """
#     if head is None:
#         return None
#     curr, prev = head, None
#     while curr is not None:
#         tmp = curr
#         curr = curr.next
#         tmp.next = prev
#         prev = tmp
#     return prev
#
# def add_list_elem(in1, in2, carry):
#     """addition of two nodes with carry_in and carry_out
#     """
#     in1_val = in1.value if in1 else 0
#     in2_val = in2.value if in2 else 0
#     tmp = in1_val + in2_val + carry
#     print('tmp', tmp)
#     return ListNode(tmp % 10000), tmp // 10000


def solution(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    result = ListNode(0)
    pointer = result

    while l1 or l2 or carry:
        first_num = l1.value if l1.value else 0
        second_num = l2.value if l2.value else 0

        summation = first_num + second_num + carry

        num = summation % 10
        carry = summation // 10

        pointer.next = ListNode(num)

        pointer = pointer.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result.next


solution(ListNode([9876, 5432, 1999]), ListNode([1, 8001]))
