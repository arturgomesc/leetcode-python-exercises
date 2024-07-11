from typing import List
from itertools import count


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = [i for i, j in zip(count(), nums) if j == target]
        if index:
            return index[0]
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


solution = Solution()
print(solution.searchInsert(nums=[1, 3, 5, 6], target=7))
