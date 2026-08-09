"""
🔄 Convert → Sort → Rebuild
===========================

This module implements a linked-list merging strategy that follows
three simple stages:

    🔗 1. Convert
       Traverse each linked list and extract its values into Python lists.

    📊 2. Sort
       Combine both collections of values and sort them together.

    🏗️ 3. Rebuild
       Create a brand-new linked list from the sorted values.

The approach intentionally separates the problem into familiar
operations: linked-list traversal, list manipulation, sorting, and
linked-list construction.

💡 Unlike approaches that directly manipulate the original nodes,
this implementation creates new `ListNode` objects for the final
merged list.

Example:

    list1 = 1 → 2 → 4
    list2 = 1 → 3 → 4

          ↓ Convert

    [1, 2, 4] + [1, 3, 4]

          ↓ Sort

    [1, 1, 2, 3, 4, 4]

          ↓ Rebuild

    1 → 1 → 2 → 3 → 4 → 4
"""
from typing     import List, Optional
from ListNode   import ListNode

class CSR:
    """
    🔄 Convert, Sort & Rebuild merger.

    This class merges two sorted linked lists by temporarily converting
    their nodes into Python lists, sorting all values together, and then
    constructing a fresh linked list from the sorted result.

    Attributes:
        first_chain:
            The head of the first linked list.

        second_chain:
            The head of the second linked list.

        head:
            The head of the newly constructed merged linked list.

        tail:
            The last node of the newly constructed merged linked list.
            Keeping track of the tail makes appending new nodes simple.
    """

    def __init__(
        self                        ,
        list1: Optional[ListNode]   ,
        list2: Optional[ListNode]   ,
    )   ->  None:
        """
        🏗️ Initialize the two linked-list chains.

        Args:
            list1:
                Head node of the first sorted linked list.

            list2:
                Head node of the second sorted linked list.
        """

        # 🔗 Keep references to both input linked-list chains.
        self.first_chain    : Optional[ListNode] = list1
        self.second_chain   : Optional[ListNode] = list2

        # 🌱 These will eventually point to the newly rebuilt list.
        #
        # Initially, no merged list exists.
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None

    def convert_to_list(
        self                        ,
        head:   Optional[ListNode]  ,
    )   ->      List[int]:
        """
        📦 Convert a linked-list chain into a Python list of values.

        The linked list is traversed one node at a time. Each node's
        value is copied into a Python list.

        Args:
            head:
                The starting node of the linked list.

        Returns:
            A Python list containing all node values in traversal order.

        Example:

            1 → 2 → 4 → None

                    ↓

               [1, 2, 4]
        """

        # 📋 Start with an empty collection for the extracted values.
        result: List[int] = []

        # 🚶 Walk through the linked list until we reach its end.
        while head:
            # 📥 Copy the current node's value into the Python list.
            result.append(head.val)

            # ➡️ Move to the next node in the chain.
            head = head.next

        return result

    def merge(self) -> Optional[ListNode]:
        """
        🔀 Merge the two linked lists using Convert → Sort → Rebuild.

        Returns:
            The head of the newly constructed sorted linked list.

        The process is divided into three clear stages:

            🔗 Convert
                Linked-list nodes → Python lists

            📊 Sort
                Combine values → sorted collection

            🏗️ Rebuild
                Sorted values → new linked list
        """

        # 🚪 If the first chain is empty, there is nothing to merge
        # with it. The second chain can be returned directly.
        if self.first_chain is None: return self.second_chain

        # 🚪 Likewise, if the second chain is empty, the first chain
        # already represents the complete result.
        if self.second_chain is None: return self.first_chain

        # ==========================================================
        # 🔗 STEP 1 — CONVERT
        # ==========================================================
        #
        # Extract the values from both linked lists into regular
        # Python lists. This temporarily moves our focus from nodes
        # and pointers to simple collections of values.

        values1: List[int] = self.convert_to_list(self.first_chain)
        values2: List[int] = self.convert_to_list(self.second_chain)

        # ==========================================================
        # 📊 STEP 2 — SORT
        # ==========================================================
        #
        # Combine both collections and let Python's built-in sorting
        # arrange every value in non-decreasing order.
        #
        # Example:
        #
        #     [1, 2, 4] + [1, 3, 4]
        #             ↓
        #     [1, 1, 2, 3, 4, 4]

        merged_values: List[int] = sorted(values1 + values2)

        # ==========================================================
        # 🏗️ STEP 3 — REBUILD
        # ==========================================================
        #
        # Start constructing a completely new linked list from the
        # sorted values.
        #
        # The first value becomes both the head and tail because
        # the list initially contains exactly one node.

        self.head = self.tail = ListNode(merged_values[0])

        # 🔨 Add every remaining value to the end of the new chain.
        for value in merged_values[1:]:
            # 🆕 Create a fresh node for the current sorted value.
            new_node = ListNode(value)

            # 🔗 Attach the new node after the current tail.
            self.tail.next = new_node

            # 📍 Move the tail forward so it always points to the
            # final node in our newly constructed chain.
            self.tail = new_node

        # 🏁 Return the beginning of the rebuilt sorted chain.
        return self.head
