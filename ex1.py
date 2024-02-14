
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)
    
    def binary_search(self, target):
        start, end = self.head, None
        while start != end:
            mid = self.get_mid(start, end)
            if mid.value == target:
                return True
            elif mid.value < target:
                start = mid.next
            else:
                end = mid
        return False

    def get_mid(self, start, end):
        slow = fast = start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        return slow

class Array:
    def __init__(self):
        self.array = []

    def append(self, value):
        self.array.append(value)

    def binary_search(self, target):
        left, right = 0, len(self.array) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == target:
                return True
            elif self.array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

# Complexity of binary search for linked lists:
# The binary search on a linked list has a time complexity of O(logn) for finding the middle element,
# but because accessing elements is linear in a linked list, the overall complexity becomes O(n) to find the mid-point repeatedly.
# Therefore, the total time complexity is O(nlogn).
