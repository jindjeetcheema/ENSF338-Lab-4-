
# Answer to Question 1: Difference Between Array Size and Capacity
'''
Size refers to the number of elements currently stored in the array, representing the actual count of data elements it holds.
Capacity refers to the total amount of space allocated for the array in memory, indicating the maximum number of elements the array can hold before needing resizing.
'''

# Answer to Question 2: What happens when an array needs to grow beyond its current capacity?
'''
When an array needs to grow, a new, larger block of memory is allocated, and all elements from the original array are copied over to this new block.
The original array is then discarded, and the pointer is updated to point to the new array location.
'''

# Case 1: Space Available After the Array
'''
Before Expansion: The array occupies a contiguous block of memory, with unused space following it.
After Expansion: The array's capacity is increased by allocating the additional space needed directly adjacent to the original end of the array.
'''

# Case 2: Memory After the Array is Occupied
'''
Before Expansion: The array is followed immediately by another variable or data structure, with no free space in between for expansion.
After Expansion: A new, larger block of memory elsewhere is allocated, and the contents of the original array are copied over. The original space is released or used for other purposes.
'''

# Answer to Question 3: Techniques to Amortize the Cost of Array Expansion
'''
Real-world array implementations often use techniques such as doubling the size of the array upon reaching capacity or using a growth factor less than double (e.g., 1.5 times the current capacity).
These strategies reduce the number of resizes needed as the array grows, thereby amortizing the cost over many operations.
'''