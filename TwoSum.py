class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        for i in range(len(nums) - 1, 0, -1):
            if (target - nums[i]) in nums[:i]:
                print([nums.index(target - nums[i]), i])


# test code
nums = [2, 7, 11, 15]
target = 9

s = Solution()
s.twoSum(nums, target)