"""
You’re given the pointer to the head nodes of two sorted linked lists. The data
in both lists will be sorted in ascending order. Change the next pointers to
obtain a single, merged linked list which also has data in ascending order.
Either head pointer given may be null meaning that the corresponding list is
empty.

Input Format
You have to complete the Node* MergeLists(Node* headA, Node* headB) method which
takes two arguments - the heads of the two sorted linked lists to merge. You
should NOT read any input from stdin/console.

Output Format
Change the next pointer of individual nodes so that nodes from both lists are
merged into a single list. Then return the head of this merged list. Do NOT
print anything to stdout/console.

"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


# with recursion
def MergeList2(headA, headB):
    if not headA and not headB:
        return None
    if not headA:
        return headB
    if not headB:
        return headA
    if headA.data < headB.data:
        curr = headA
        curr.next = MergeList2(headA.next, headB)
    else:
        curr = headB
        curr.next = MergeList2(headA, headB.next)

    return curr


# without recursion
def MergeLists1(headA, headB):
    if headA and headB:
        headC = Node(min(headA.data, headB.data))
        if headA.data == headC.data:
            currA, currB = headA.next, headB
        else:
            currA, currB = headA, headB.next
    elif headA:
        headC = Node(headA.data)
        currA, currB = headA.next, headB
    elif headB:
        headC = Node(headB.data)
        currA, currB = headA, headB.next
    else:
        return None
    currC = headC

    while currA or currB:
        if currA and currB:
            currC.next = Node(min(currA.data, currB.data))
            if currC.next.data == currA.data:
                currA = currA.next
            else:
                currB = currB.next
        elif currA:
            currC.next = Node(currA.data)
            currA = currA.next
        else:
            currC.next = Node(currB.data)
            currB = currB.next

        currC = currC.next

    return headC
