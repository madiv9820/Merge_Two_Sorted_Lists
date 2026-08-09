"""
👥 Two Pointers, One New Chain
==============================

This module merges two sorted linked lists using two moving pointers
while constructing a completely new linked list.

The idea can be visualized as two runners moving through two already
sorted chains:

    Chain 1:  1 → 2 → 4
              ↑
             ptr1

    Chain 2:  1 → 3 → 4
              ↑
             ptr2

At every step, the pointers look at their current values. The smaller
value is added to the new chain, and that pointer moves forward.

The process continues until one chain is exhausted. Any remaining
nodes from the other chain are then copied into the new chain.

💡 Important:
This implementation creates NEW `ListNode` objects for the result.
The original linked-list nodes are never reused or modified.

Example:

    list1 = 1 → 2 → 4
    list2 = 1 → 3 → 4

                ↓ Compare

    1 → 1 → 2 → 3 → 4 → 4

                ↓

         New Linked List
"""
from typing     import Optional
from ListNode   import ListNode

class TPNC:
    """
    👥 Two Pointers, New Chain.

    Merges two sorted linked lists by using one pointer for each input
    list and constructing a brand-new linked list from the values
    encountered in sorted order.

    Attributes:
        first_chain:
            Head of the first sorted linked list.

        second_chain:
            Head of the second sorted linked list.

        head:
            Head of the newly constructed merged linked list.

        tail:
            Last node of the newly constructed merged linked list.
            Keeping a tail pointer allows new nodes to be appended in
            constant time.
    """

    def __init__(
        self                        ,
        list1: Optional[ListNode]   ,
        list2: Optional[ListNode]   ,
    )   -> None:
        """
        🏗️ Initialize the two input linked-list chains.

        Args:
            list1:
                Head of the first sorted linked list.

            list2:
                Head of the second sorted linked list.
        """

        # 🔗 Preserve references to both input chains.
        self.first_chain    : Optional[ListNode] = list1
        self.second_chain   : Optional[ListNode] = list2

        # 🌱 The new merged chain starts empty.
        #
        # As nodes are created, `head` will remember where the chain
        # begins, while `tail` will keep track of its latest node.
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None

    def merge(self) -> Optional[ListNode]:
        """
        🔀 Merge both sorted chains into a brand-new linked list.

        Returns:
            The head of the newly created sorted linked list.

        The merge proceeds by:

            👥 1. Positioning one pointer on each input list.
            ⚖️ 2. Comparing the values at both pointers.
            🆕 3. Creating a new node with the smaller value.
            ➡️ 4. Advancing the pointer from which the value came.
            🏁 5. Copying the remaining values once one list ends.
        """

        # 🚪 If the first chain is empty, there is nothing to compare.
        # Return the second chain directly.
        if not self.first_chain: return self.second_chain

        # 🚪 Likewise, if the second chain is empty, the first chain
        # already represents the complete result.
        if not self.second_chain: return self.first_chain

        # 🌱 Start with a completely empty result chain.
        #
        # This also makes `merge()` safe to call again on the same
        # object without retaining the previous result.
        self.head = self.tail = None

        # 👥 Place one pointer at the beginning of each input chain.
        #
        # Think of these as two explorers walking through two
        # sorted paths, deciding which value should come next.
        ptr1: Optional[ListNode] = self.first_chain
        ptr2: Optional[ListNode] = self.second_chain

        # ==========================================================
        # ⚖️ PHASE 1 — COMPARE BOTH CHAINS
        # ==========================================================
        #
        # As long as both pointers are valid, both chains still have
        # values available for comparison.
        while ptr1 and ptr2:

            # 🧮 This will hold the value selected for the new chain.
            new_value: int

            # ⚖️ Compare the current values of both pointers.
            #
            # Using <= ensures that when values are equal, the value
            # from the first chain is selected first.
            if ptr1.val <= ptr2.val:

                # 🥇 The first chain provides the next smallest value.
                new_value = ptr1.val

                # ➡️ Move pointer 1 forward because its current value
                # has now been consumed.
                ptr1 = ptr1.next

            else:

                # 🥈 The second chain provides the next smallest value.
                new_value = ptr2.val

                # ➡️ Move pointer 2 forward because its current value
                # has now been consumed.
                ptr2 = ptr2.next

            # 🆕 Create a completely new node for the selected value.
            #
            # The original nodes remain untouched.
            new_node: ListNode = ListNode(new_value)

            # 🌱 If this is the very first node, it becomes both the
            # beginning and the end of our new chain.
            if not self.head:
                self.head = self.tail = new_node

            else:
                # 🔗 Attach the new node after the current tail.
                self.tail.next = new_node

                # 📍 Move the tail forward to the newly added node.
                self.tail = new_node

        # ==========================================================
        # 🏁 PHASE 2 — FINISH THE FIRST CHAIN
        # ==========================================================
        #
        # If ptr1 still has nodes, ptr2 has already reached the end.
        # Because list1 was sorted, every remaining value can simply
        # be appended in its existing order.
        while ptr1:

            # 🆕 Create a fresh node using the remaining value.
            new_node = ListNode(ptr1.val)

            # ➡️ Advance pointer 1 before processing the next node.
            ptr1 = ptr1.next

            # 🔗 Append the new node to the merged chain.
            self.tail.next  = new_node
            self.tail       = new_node

        # ==========================================================
        # 🏁 PHASE 3 — FINISH THE SECOND CHAIN
        # ==========================================================
        #
        # If ptr2 still has nodes, ptr1 has already reached the end.
        # The remaining values are already sorted, so they can be
        # appended directly.
        while ptr2:

            # 🆕 Create a fresh node for the remaining value.
            new_node = ListNode(ptr2.val)

            # ➡️ Advance pointer 2 to the next node.
            ptr2 = ptr2.next

            # 🔗 Append the new node to the merged chain.
            self.tail.next  = new_node
            self.tail       = new_node

        # 🏁 Return the beginning of the newly constructed chain.
        return self.head
