from Node import ListNode

def add_numbers(l1, l2):
    temp = ListNode(0, None)
    current = temp
    carry = 0

    while l1 or l2 or carry != 0:
        digit1 = l1.val if l1 else 0
        digit2 = l2.val if l2 else 0

        sum = digit1 + digit2 + carry
        digit = sum % 10
        carry = sum // 10

        new_node = ListNode(digit, None)
        current.next = new_node
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    result = temp.next
    temp.next = None
    return result