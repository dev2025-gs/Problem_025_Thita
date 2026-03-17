# Definition for singly-linked list.
# Each node contains a value and a reference to the next node.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution class containing the merge function
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # If either list is empty, return the other list
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # Compare the values of the current nodes
        # Recursively merge the rest of the lists
        if list1.val <= list2.val:
            # If list1's value is smaller or equal, attach it to the merged list
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # If list2's value is smaller, attach it to the merged list
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2


# Helper function to build a linked list from a Python list
# Takes a list of values and returns the head of a linked list
def build_list(arr):
    dummy = ListNode(0)  # Dummy node to simplify list construction
    current = dummy
    for num in arr:
        current.next = ListNode(num)  # Create a new node for each value
        current = current.next        # Move to the next node
    return dummy.next  # Return the real head (skip dummy)


# Helper function to print a linked list
# Prints the values in the linked list in order
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")  # Print current node's value
        current = current.next           # Move to the next node
    print("None")  # Indicate end of list


# Example usage
if __name__ == "__main__":
    # Create two sorted linked lists from Python lists
    list1 = build_list([1, 2, 4])
    list2 = build_list([1, 3, 4])

    print("List 1:")
    print_list(list1)  # Print first list

    print("List 2:")
    print_list(list2)  # Print second list

    # Merge the two lists using Solution
    sol = Solution()
    merged = sol.mergeTwoLists(list1, list2)

    print("Merged List:")
    print_list(merged)  # Print merged list