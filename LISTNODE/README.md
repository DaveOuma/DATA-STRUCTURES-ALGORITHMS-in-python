### Explanation

In this implementation, we utilize a `ListNode` class to model nodes within a linked list. Each node encapsulates a value (`val`) and a reference to the next node (`next`).

The `mergeTwoLists` function is designed to merge two sorted linked lists, `l1` and `l2`, into a single sorted linked list.

To streamline the merging process, we introduce a dummy node. The `current` pointer starts at this dummy node and facilitates the construction of the merged list.

We traverse both input lists simultaneously, comparing the values of respective nodes. The smaller value is appended to the merged list, and the corresponding pointer advances.

After exhaustively traversing both lists, any remaining nodes from either `l1` or `l2` are appended to the merged list.

Finally, we return the head of the merged list, excluding the dummy node, and print out the elements for verification.

This approach effectively merges two sorted linked lists, ensuring the resultant list remains sorted in ascending order.

