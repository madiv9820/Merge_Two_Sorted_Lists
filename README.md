# [🔗 Two Sorted Streams, One Perfect Chain! 🚀](https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150)

### 📖 The Story

Imagine two queues of numbers standing in perfect order, waiting to enter the same line. 🧍‍♂️🧍‍♀️

Your job is to bring them together into ***one single queue that remains sorted from start to finish***. The catch? These aren't ordinary numbers—they're nodes connected through linked lists, and you need to preserve and reuse those existing nodes. 🔗✨

### 🎯 The Challenge

You are given the heads of **two sorted linked** lists, **`list1`** and **`list2`**.

Merge the two lists into **one sorted linked list** by splicing together the nodes from the original lists.

Finally, return the ***head of the newly merged linked list***. 🚀

Both lists are sorted in **non-decreasing order**, meaning every node's value is greater than or equal to the value before it.

- **🧪 Example 1 — Two Lists Become One**
    
    ```
    Input   :   list1 = [1,2,4]
                list2 = [1,3,4]

    Output  :   [1,1,2,3,4,4]
    ```
    
    Two sorted streams come together to form one perfectly ordered stream. 🎯

- **🧪 Example 2 — Both Lists Are Empty**
    
    ```
    Input   :   list1 = []
                list2 = []

    Output  :   []
    ```
    
    Nothing to merge, so the result is an empty list. 🫥

- **🧪 Example 3 — One List Is Empty**
    
    ```
    Input   :   list1 = []
                list2 = [0]

    Output  :   [0]
    ```
    
    When one list has no nodes, the existing list simply becomes the result. 🔗

#### 📌 Constraints

- 🔢 The total number of nodes across both lists is between **`0`** and **`50`**.
- 📏 Each node value satisfies **`-100 <= Node.val <= 100`**.
- 📈 Both **`list1`** and **`list2`** are sorted in **non-decreasing order**.
- 🔗 The merged list should be formed by **splicing the existing nodes** together.
---

### 🧠 Approaches

There are several ways to merge two sorted linked lists, and each approach highlights a different way of thinking about the problem. We start with a straightforward **Convert → Sort → Rebuild** strategy, then take advantage of the fact that the lists are already sorted with **Two Pointers**, and finally eliminate unnecessary extra space by performing the merge **in-place** using the original nodes. 🔗✨

#### 📋 Approach 1 — Convert, Sort & Rebuild

- **💡 Intuition**

    Instead of working directly with linked-list pointers, temporarily convert both linked lists into regular Python lists. Combine their values, sort everything together, and then construct a brand-new linked list from the sorted values.

    It trades extra memory for simplicity. 🧩

- **🔄 Steps**

    1. Traverse **`list1`** and collect all values into a Python list.
    2. Traverse **`list2`** and collect all values into another Python list.
    3. Combine both collections.
    4. Sort the combined values.
    5. Create a new linked list from the sorted values.
    6. Return the head of the newly created list.

- **📝 Pseudocode**

    ```
    convert list1 → values1 
    convert list2 → values2 
    
    merged_values = sort(values1 + values2) 
    
    create new linked list from merged_values 
    
    return new list
    ```

- **⏱️ Complexity**

    - **Time: `O((n + m) log(n + m))`**
    - **Space: `O(n + m)`**

    Where **`n`** and **`m`** are the number of nodes in the two lists.

#### 👥 Approach 2 — Two Pointers, New Chain

- **💡 Intuition**

    Both input lists are already sorted, so there is no need to sort their values again.

    Place one pointer at the beginning of each list and compare their current values. The smaller value belongs next in the result. Create a **new node** with that value and move the corresponding pointer forward.

    It's essentially a friendly race between two sorted chains. 🏁🔗

- **🔄 Steps**

    1. Place **`ptr1`** at the beginning of **`list1`**.
    2. Place **`ptr2`** at the beginning of **`list2`**.
    3. Compare **`ptr1.val`** and **`ptr2.val`**.
    4. Add the smaller value to the new linked list.
    5. Advance the pointer that supplied the value.
    6. Repeat while both pointers are valid.
    7. Append the remaining nodes' values from whichever list is not exhausted.
    8. Return the head of the new chain.

- **📝 Pseudocode**

    ```
    ptr1 = list1 
    ptr2 = list2 
    result = empty list 

    while ptr1 and ptr2: 
        if ptr1.val <= ptr2.val: 
            append new node(ptr1.val) 
            ptr1 = ptr1.next 
        else: 
            append new node(ptr2.val) 
            ptr2 = ptr2.next 

    while ptr1: 
        append new node(ptr1.val) 
        ptr1 = ptr1.next 

    while ptr2: 
        append new node(ptr2.val) 
        ptr2 = ptr2.next 
        
    return result
    ```

- **⏱️ Complexity**
    
    - **Time: `O(n + m)`**
    - **Space: `O(n + m)`**

    The lists are traversed only once, but a new node is created for every value in the merged result.

#### 🔗 Approach 3 — Two Chains, In-Place Merge

- **💡 Intuition**

    This approach takes the idea from the two-pointer solution one step further.

    Since the original lists are already sorted, we don't need to create new nodes at all. We can simply **reuse the existing nodes** and reconnect their **`next`** pointers in the correct order.

    Two chains enter the merge, and pointer rewiring turns them into one sorted chain. 🪢⚡

- **🔄 Steps**

    1. Handle the case where either list is empty.
    2. Compare the first nodes of both lists.
    3. Use the smaller node as the head of the merged list.
    4. Maintain a **`tail`** pointer at the end of the merged chain.
    5. Compare the current nodes of both lists.
    6. Attach the smaller existing node after **`tail`**.
    7. Move the selected list's pointer forward.
    8. Continue until one list is exhausted.
    9. Attach the remaining portion of the other list.
    10. Return the merged list's head.

- **📝 Pseudocode**

    ```
    if list1 is empty: 
        return list2 

    if list2 is empty: 
        return list1 

    choose smaller first node as head 
    tail = head 

    while list1 and list2: 
        if list1.val <= list2.val: 
            tail.next = list1 
            list1 = list1.next 
        else: 
            tail.next = list2 
            list2 = list2.next 
        
        tail = tail.next 

    attach remaining list1 or list2 

    return head
    ```

- **⏱️ Complexity**
    
    - **Time: `O(n + m)`**
    - **Space: `O(1)`**
    
    Every node is visited at most once, and no additional linked-list nodes or collections are created. 🏆

### ⚖️ Quick Comparison

| Approach                          | Core Idea                  |                Time | Extra Space | New Nodes |
| --------------------------------- | -------------------------- | ------------------: | ----------: | --------: |
| 📋 **Convert, Sort & Rebuild**    | Convert → Sort → Rebuild   | **`O((n+m) log(n+m))`** |    **`O(n+m)`** |     ✅ Yes |
| 👥 **Two Pointers, New Chain**    | Compare → Copy → Advance   |            **`O(n+m)`** |    **`O(n+m)`** |     ✅ Yes |
| 🔗 **Two Chains, In-Place Merge** | Compare → Rewire → Advance |            **`O(n+m)`** |      **`O(1)`** |      ❌ No |

### 🏆 Takeaway

The three approaches form a nice progression:

**📋 Simplify the data → 👥 Exploit sorted order → 🔗 Exploit sorted order + existing nodes**

The third approach is the most space-efficient and is the standard optimal solution for this problem.

---
