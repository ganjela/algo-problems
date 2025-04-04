from Node import ListNode

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