class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # counter for number of elements not equal to val
        k = 0
        for num in nums:
            if num != val:
                k += 1
        for _ in range(len(nums) - k):
            nums.remove(val)
        return k
        