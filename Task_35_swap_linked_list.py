from Node import ListNode
"""
1 -> 2 -> 3 -> 4

Update the pointers to swap the nodes:
Adjust current.next to point to the remaining list.
Point current.next (second node) back to `current` as the new first node in the pair.
Update previous to link to the swapped pair.
Move current and previous pointers to the next pair.
   
`2 -> 1 -> 3 -> 4`.
`2 -> 1 -> 4 -> 3`.
"""

def swap_nodes(head):
    temp = ListNode(0, head)
    previous = temp
    current = head

    while current and current.next:
        next_pair = current.next.next
        second = current.next

        second.next = current
        current.next = next_pair
        previous.next = second

        previous = current
        current = next_pair

    return temp.next