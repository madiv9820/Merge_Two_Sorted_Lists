"""
🎯 Merge Two Sorted Linked Lists — Solution Entry Point
=======================================================

This module provides the main `Solution` class required by LeetCode.

Instead of placing every implementation directly inside
`mergeTwoLists()`, the actual algorithms are delegated to
three dedicated approach classes:

    📋 CSR
       Convert → Sort → Rebuild

    👥 TPNC
       Two Pointers → New Chain

    🔗 TCIM
       Two Chains → In-Place Merge

The `Solution` class therefore acts as a clean interface between
the LeetCode problem and the individual algorithm implementations.

🏆 The selected implementation is `TCIM`, the in-place approach,
which runs in O(n + m) time and uses O(1) auxiliary space.
"""
from typing         import Optional
from ListNode       import ListNode
from .approaches    import CSR, TPNC, TCIM


class Solution:
    """
    🎯 LeetCode solution interface for merging two sorted linked lists.

    The class exposes the method expected by LeetCode while keeping
    the actual merging strategies organized inside separate modules.

    This separation makes the implementations easier to:

        🧪 Test independently
        📖 Understand individually
        ⚖️ Compare against one another
        🔧 Maintain or improve later
    """

    def mergeTwoLists(
        self                        ,
        list1: Optional[ListNode]   ,
        list2: Optional[ListNode]   ,
    ) -> Optional[ListNode]:
        """
        🔗 Merge two sorted linked lists.

        Args:
            list1:
                Head of the first sorted linked list.

            list2:
                Head of the second sorted linked list.

        Returns:
            The head of the merged sorted linked list.

        The method prepares all three available implementations,
        with `TCIM` being the selected strategy for the final result.

        🏆 Selected approach:
            Two Chains, In-Place Merge

        This approach reuses the existing nodes instead of creating
        a completely new linked list.
        """

        # ==========================================================
        # 📋 APPROACH 1 — CONVERT, SORT & REBUILD
        # ==========================================================
        #
        # Converts both linked lists into Python lists, sorts all
        # values together, and rebuilds a new linked list.
        #
        # This approach is kept here so all strategies have a
        # consistent entry point and can be easily compared.
        approach1: CSR = CSR(list1, list2)

        # ==========================================================
        # 👥 APPROACH 2 — TWO POINTERS, NEW CHAIN
        # ==========================================================
        #
        # Uses two pointers to compare values from both lists while
        # constructing a completely new linked list.
        approach2: TPNC = TPNC(list1, list2)

        # ==========================================================
        # 🔗 APPROACH 3 — TWO CHAINS, IN-PLACE MERGE
        # ==========================================================
        #
        # Reuses the original nodes and reconnects their `next`
        # pointers to form the final sorted chain.
        #
        # 🏆 This is the selected implementation because it achieves
        # O(n + m) time with O(1) auxiliary space.
        approach3: TCIM = TCIM(list1, list2)

        # 🚀 Delegate the actual work to the selected approach.
        #
        # Only TCIM is executed here. This is particularly important
        # because TCIM modifies the original linked-list structure
        # in place.
        return approach3.merge()
    