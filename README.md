# Merge Two Sorted Linked Lists

## 🧩 Problem Description

You are given the heads of two **sorted linked lists**, `list1` and `list2`.

Merge the two lists into one **sorted linked list**. The merged list should be made by **splicing together the nodes** of the first two lists.

Return the **head of the merged linked list**.
https://thita.ai/problems/merge-two-sorted-lists

---

## 📥 Examples

### Example 1
**Input:**
```
list1 = [1,2,4]
list2 = [1,3,4]
```
**Output:**
```
[1,1,2,3,4,4]
```

---

### Example 2
**Input:**
```
list1 = []
list2 = []
```
**Output:**
```
[]
```

---

### Example 3
**Input:**
```
list1 = []
list2 = [0]
```
**Output:**
```
[0]
```

---

## 📌 Constraints

- The number of nodes in both lists is in the range `[0, 50]`
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing order**

---

## 💡 Approach

We use a **two-pointer technique** to iterate through both linked lists:

1. Create a **dummy node** to simplify edge cases.
2. Maintain a pointer (`current`) to build the merged list.
3. Compare the values of nodes from both lists:
   - Attach the smaller node to `current.next`
   - Move the corresponding pointer forward
4. Continue until one list is exhausted.
5. Attach the remaining nodes from the non-empty list.

---

## ⚙️ Algorithm

- Initialize a dummy node.
- Use two pointers (`l1`, `l2`) for both lists.
- Iterate while both pointers are not null:
  - Compare values and link the smaller node.
- Append the remaining nodes.
Source: https://www.geeksforgeeks.org/dsa/merge-two-sorted-linked-lists/
---

## 🧮 Complexity Analysis

- **Time Complexity:** `O(n + m)`  
  - Where `n` and `m` are the lengths of the two lists.

- **Space Complexity:** `O(1)`  
  - No extra space is used (in-place merging).

---

## 🧪 Edge Cases Considered

- Both lists are empty
- One list is empty
- Lists of different lengths
- Duplicate values in lists

---

## 🏁 Summary

This problem demonstrates efficient merging using **pointer manipulation** without creating new nodes. The dummy node simplifies implementation and ensures clean handling of edge cases.

---

## 🚀 Tags

`Linked List` `Two Pointers` `Recursion` `Iteration`
