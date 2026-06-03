class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # length of the list
        n = len(arr)
        # set max to be the last element
        max_so_far = arr[-1]
        # iterate backwards starting from second to last
        for i in range(n-2,-1,-1):
            # copy the current value
            temp = arr[i]
            # update current value to max
            arr[i] = max_so_far
            # update max if necessary
            max_so_far = max(temp, max_so_far)
        # set last elment to -1
        arr[len(arr) - 1] = -1
        return arr