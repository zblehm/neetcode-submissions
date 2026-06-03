class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                # update the number of most consecutive 1s if necessary
                if count > max_consecutive:
                    max_consecutive = count
                # reset the count
                count = 0
        if count > max_consecutive:
            max_consecutive = count
        return max_consecutive
        