from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] + nums[i+1] == target:
                return [i, nums.index(nums[i]) + nums[i+1]]



