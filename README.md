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