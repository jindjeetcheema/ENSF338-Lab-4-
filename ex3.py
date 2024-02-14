# Explanation of growth strategy (as a comment)
"""
Python lists are implemented as dynamic arrays. When a list's capacity is exceeded,
it is resized with a growth factor to accommodate additional elements efficiently.
This strategy minimizes the number of memory allocations required as the list grows.
"""

# Test code for observing capacity changes
import sys

previous_size = 0
for i in range(64):
    lst = [0] * i
    current_size = sys.getsizeof(lst)
    if current_size != previous_size:
        print(f"Capacity changed at {i} elements: {current_size} bytes")
    previous_size = current_size

# Sample for time measurement (pseudo-code, actual implementation will vary)
import timeit

def measure_append_time(lst, iterations=1000):
    times = [timeit.timeit(lambda: lst.append(0), number=1) for _ in range(iterations)]
    return times

# Example usage of measure_append_time and plotting results (pseudo-code)
# times_for_S_to_S1 = measure_append_time(lst_with_size_S)
# times_for_S1_to_S = measure_append_time(lst_with_size_S1)

# Plotting code using matplotlib (pseudo-code)
# import matplotlib.pyplot as plt
# plt.hist(times_for_S_to_S1, alpha=0.5, label='S to S+1')
# plt.hist(times_for_S1_to_S, alpha=0.5, label='S-1 to S')
# plt.legend()
# plt.show()

# Include your discussion as comments in the code
"""
Discussion:
The time it takes for a list to grow from size S to S+1 can be significantly different
from growing from S-1 to S due to the resizing strategy employed by Python lists. When
resizing occurs, a new, larger array is allocated, and elements are copied over, which
can add overhead compared to adding an element without needing to resize.
"""
