#!/usr/bin/python3

# Define a class to represent nodes in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize node value and next pointer
        self.val = val
        self.next = next

# Define a function to merge two sorted linked lists into a single sorted linked list
def mergeTwoLists(l1, l2):
    # Create a dummy node to simplify the merging process
    dummy = ListNode()
    # Initialize a current pointer to the dummy node
    current = dummy

    # Iterate through both linked lists simultaneously
    while l1 and l2:
        # Compare the values of nodes in both lists
        if l1.val < l2.val:
            # If the value in l1 is smaller, append l1 to the merged list
            current.next = l1
            # Move l1 pointer to the next node
            l1 = l1.next
        else:
            # If the value in l2 is smaller or equal, append l2 to the merged list
            current.next = l2
            # Move l2 pointer to the next node
            l2 = l2.next
        # Move the current pointer to the next node in the merged list
        current = current.next

    # Append the remaining nodes of l1 or l2 to the merged list
    if l1:
        current.next = l1
    else:
        current.next = l2

    # Return the head of the merged list (excluding the dummy node)
    return dummy.next

# Test case:
# Define two sorted linked lists
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
# Merge the two lists and store the head of the merged list
merged_list = mergeTwoLists(l1, l2)

# Print the merged list for verification
while merged_list:
    print(merged_list.val, end=" -> ")
    # Move to the next node in the merged list
    merged_list = merged_list.next

