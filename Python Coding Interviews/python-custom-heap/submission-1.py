import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    # using tuple with (priority, value)

    heap = []

    for num in nums:
        pair = (-num, num)
        heapq.heappush(heap, pair)

    reverse_sorted_list  =[]
    while heap:
        pair = heapq.heappop(heap)
        reverse_sorted_list.append(pair[1])

    return reverse_sorted_list
    




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
