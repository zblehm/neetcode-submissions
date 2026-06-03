class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # set max to be the last element
        max = arr[-1]
        # iterate backwards starting from second to last
        for i in range(len(arr)-2,-1,-1):
            # copy the current value
            temp = arr[i]
            # update current value to max
            arr[i] = max
            # update max if necessary
            if temp > max:
                max = temp
        # set last elment to -1
        arr[len(arr) - 1] = -1
        return arr