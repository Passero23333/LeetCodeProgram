class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(0, n):
            difference = target - nums[i]
            if difference in nums and nums.index(difference) != i:
                return [i, nums.index(difference)]
