import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    # reverse sort using max heap concept
    
    # make a list of the negated values
    negated_nums = [-num for num in nums]
    # create a heap 
    heapq.heapify(negated_nums)
    # empty list to store the descending sorted values
    reverse_sort_list = []
    while negated_nums:
        # append the double negated = original value
        reverse_sort_list.append(-heapq.heappop(negated_nums))
    return reverse_sort_list





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
