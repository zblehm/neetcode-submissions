class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # length of the list
        n = len(arr)
        # set max to be -1, so last element will be -1
        max_so_far = -1
        # iterate backwards starting from second to last
        for i in range(n-1,-1,-1):
            # copy the current value
            temp = arr[i]
            # update current value to max
            arr[i] = max_so_far
            # update max if necessary
            max_so_far = max(temp, max_so_far)
        return arr