"""
🔗 Two Chains, One In-Place Merge
=================================

This module merges two sorted linked lists by directly rewiring
their existing nodes.

Unlike approaches that create a separate result list, this strategy
does NOT allocate any new `ListNode` objects.

Instead, the existing nodes from both chains are carefully connected
together in sorted order.

Think of it as two already-organized chains being woven into one:

    Chain 1: 1 → 2 → 4
    Chain 2: 1 → 3 → 4

                ↓ Rewire existing links

    Result:    1 → 1 → 2 → 3 → 4 → 4

💡 The key idea is simple:

    👀 Compare the front nodes
    🔗 Attach the smaller existing node
    ➡️ Advance the chain that supplied that node
    🔁 Repeat until one chain is exhausted
    🏁 Attach whatever remains

No new nodes. No temporary value list.
Just careful pointer manipulation. 🪢✨
"""
from typing import Optional
from ListNode import ListNode

class TCIM:
    """
    🔗 Two Chains, In-Place Merge.

    Merges two sorted linked lists by reusing and reconnecting their
    existing nodes rather than constructing a new linked list.

    Attributes:
        first_chain:
            Head of the remaining portion of the first linked list.

        second_chain:
            Head of the remaining portion of the second linked list.

        head:
            Head of the merged linked list.

        tail:
            Last node currently connected to the merged linked list.
            This allows the next selected node to be attached directly.
    """

    def __init__(
        self                        ,
        list1: Optional[ListNode]   ,
        list2: Optional[ListNode]   ,
    ) -> None:
        """
        🏗️ Initialize the two linked-list chains.

        Args:
            list1:
                Head of the first sorted linked list.

            list2:
                Head of the second sorted linked list.
        """

        # 🔗 Keep references to both original chains.
        self.first_chain    : Optional[ListNode] = list1
        self.second_chain   : Optional[ListNode] = list2

        # 🌱 The merged chain starts empty.
        #
        # `head` will remember where the merged chain begins,
        # while `tail` will track its current final node.
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None

    def merge(self) -> Optional[ListNode]:
        """
        🔀 Merge both sorted chains by rewiring existing nodes.

        Returns:
            The head of the merged linked list.

        The original nodes are reused directly. The method only changes
        their `next` references to create the final sorted chain.
        """

        # 🚪 If either chain is empty, the other chain already represents
        # the complete sorted result.
        if not self.first_chain : return self.second_chain
        if not self.second_chain: return self.first_chain

        # ==========================================================
        # 🏁 STEP 1 — CHOOSE THE FIRST NODE
        # ==========================================================
        #
        # Before entering the main merge loop, we need to establish
        # the first node of our merged chain.
        #
        # Whichever chain has the smaller first value provides the
        # first node. Importantly, we REUSE that existing node.
        if self.first_chain.val <= self.second_chain.val:

            # 🥇 The first chain starts with the smaller value.
            self.head = self.tail = self.first_chain

            # ➡️ Move the first chain forward.
            #
            # Its current node has already been placed into the result.
            self.first_chain = self.first_chain.next

        else:

            # 🥈 The second chain starts with the smaller value.
            self.head = self.tail = self.second_chain

            # ➡️ Move the second chain forward because its current
            # node has now become part of the merged chain.
            self.second_chain = self.second_chain.next

        # ==========================================================
        # 🔄 STEP 2 — WEAVE BOTH CHAINS TOGETHER
        # ==========================================================
        #
        # Both chains still contain nodes, so we can continue comparing
        # their current values.
        #
        # Every iteration:
        #
        #     👀 Compare
        #     🔗 Attach smaller existing node
        #     📍 Move tail
        #     ➡️ Advance the selected chain
        #
        # No new ListNode is created here.
        while self.first_chain and self.second_chain:

            # ⚖️ Compare the current nodes of both chains.
            if self.first_chain.val <= self.second_chain.val:

                # 🥇 The first chain provides the next node.
                #
                # Rewire the current tail so it points directly to
                # this EXISTING node.
                self.tail.next = self.first_chain

                # 📍 This node is now the last node in our merged chain.
                self.tail = self.first_chain

                # ➡️ Move forward in the first chain.
                self.first_chain = self.first_chain.next

            else:

                # 🥈 The second chain provides the next node.
                #
                # Again, we simply reconnect an existing node rather
                # than allocating a new one.
                self.tail.next = self.second_chain

                # 📍 Update the tail to the newly attached node.
                self.tail = self.second_chain

                # ➡️ Move forward in the second chain.
                self.second_chain = self.second_chain.next

        # ==========================================================
        # 🏁 STEP 3 — ATTACH REMAINING FIRST CHAIN
        # ==========================================================
        #
        # If nodes remain in the first chain, the second chain is
        # already exhausted.
        #
        # Because the first chain was sorted, every remaining node
        # can be attached directly in its existing order.
        while self.first_chain:

            # 🔗 Connect the current tail to the remaining node.
            self.tail.next = self.first_chain

            # 📍 Move the tail to the newly attached node.
            self.tail = self.first_chain

            # ➡️ Continue through the remaining first-chain nodes.
            self.first_chain = self.first_chain.next

        # ==========================================================
        # 🏁 STEP 4 — ATTACH REMAINING SECOND CHAIN
        # ==========================================================
        #
        # The same logic applies if nodes remain in the second chain.
        while self.second_chain:

            # 🔗 Attach the remaining existing node directly.
            self.tail.next = self.second_chain

            # 📍 Move the tail forward.
            self.tail = self.second_chain

            # ➡️ Continue through the second chain.
            self.second_chain = self.second_chain.next

        # 🏆 The merged chain is complete!
        #
        # `head` still points to the very first node, while every
        # subsequent node has been connected through `next`.
        return self.head
    