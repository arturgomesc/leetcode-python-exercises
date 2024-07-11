from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i + 1)  # remove the duplicate
            else:
                i += 1  # move to the next element only if not a duplicate
        return len(nums)

solution = Solution()
print(solution.removeDuplicates([1, 1, 2, 2, 3]))
