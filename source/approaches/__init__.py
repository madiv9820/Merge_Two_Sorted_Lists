"""
🧩 Linked List Merge — Approach Package
=======================================

This package brings together all implementations for the
"Merge Two Sorted Linked Lists" problem.

Each approach represents a different way of thinking about
the same problem:

    📋 CSR  → Convert, Sort & Rebuild
    👥 TPNC → Two Pointers, New Chain
    🔗 TCIM → Two Chains, In-Place Merge

Keeping the implementations exposed through this package-level
`__init__.py` makes them easier to import and compare from the
rest of the project.

For example:

    from .approaches import CSR, TPNC, TCIM

This keeps consumers of the package from needing to know the
individual module filenames.
"""


# 📋 Convert → Sort → Rebuild
#
# Converts both linked lists into Python lists, combines and sorts
# their values, then rebuilds the result as a new linked list.
from .Convert_Sort_Rebuild      import CSR


# 👥 Two Pointers → New Chain
#
# Uses two pointers to compare the input chains while constructing
# a completely new linked list from the selected values.
from .Two_Pointers_New_Chain    import TPNC


# 🔗 Two Chains → In-Place Merge
#
# Uses two pointers to merge the lists by reconnecting their
# existing nodes directly, without creating a new linked list.
from .Two_Chains_Inplace_Merge  import TCIM


# 📦 Public API
#
# `__all__` defines the classes that should be considered the
# public interface of this approaches package.
#
# This also makes the available strategies immediately discoverable:
#
#     CSR  → Convert, Sort & Rebuild
#     TPNC → Two Pointers, New Chain
#     TCIM → Two Chains, In-Place Merge
__all__ = ["CSR", "TPNC", "TCIM"]
