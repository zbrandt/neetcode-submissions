class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}

        for i, num in enumerate(nums):
            difference = target - num
            if difference in previous:
                return [previous[difference], i]
            else:
                previous[num] = i
        return []