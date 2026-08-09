"""
🔗 ListNode — Fundamental Linked List Building Block
====================================================

This module defines the `ListNode` class used to construct singly
linked lists throughout the project.

A linked list is made up of individual nodes. Each node stores:

    1️⃣ `val`  → The data/value contained in the node.
    2️⃣ `next` → A reference to the next node in the chain.

For example:

    1 → 2 → 3 → None

can be represented as:

    ListNode(1)
        └── next → ListNode(2)
                        └── next → ListNode(3)
                                        └── next → None

💡 Why a separate `ListNode` class?

Keeping the node definition in one place allows every linked-list
problem to share the same consistent structure. Individual solutions
can then focus entirely on their algorithm rather than redefining
the fundamental data structure.

📌 This implementation represents a *singly linked list*, meaning
each node only knows about the node immediately following it.
"""
from typing import Optional

class ListNode:
    """
    🔗 Represents a single node in a singly linked list.

    Each node contains a value and a reference to the next node.
    Together, these references allow individual nodes to form a
    complete linked-list chain.

    Example:

        node1 = ListNode(1)
        node2 = ListNode(2)

        node1.next = node2

        Result:

            1 → 2 → None

    Attributes:
        val:
            The integer value stored inside this node.

        next:
            A reference to the next `ListNode` in the linked list.
            `None` indicates that this is currently the last node.
    """

    def __init__(
        self                                ,
        val : int                   = 0     ,
        next: Optional[ListNode]    = None  ,
    ):
        """
        🏗️ Create a new linked-list node.

        Args:
            val:
                The value to store in the node.
                Defaults to `0`.

            next:
                The next node in the linked list.
                Defaults to `None`, meaning this node is not
                connected to another node yet.

        Example:

            node = ListNode(10)

            # The node currently looks like:
            #
            #     10 → None

        Another node can later be attached:

            node.next = ListNode(20)

            # Now the chain becomes:
            #
            #     10 → 20 → None
        """

        # 📦 Store the actual value carried by this node.
        self.val: int = val

        # 🔗 Store the link to the next node.
        #
        # `None` means there is currently no node after this one.
        # This is also how we identify the tail of a singly linked list.
        self.next: Optional[ListNode] = next
