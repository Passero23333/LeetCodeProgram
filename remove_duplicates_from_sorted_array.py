class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        else:
            index = 0
            for i in range(1, n):
                if nums[index] != nums[i]:
                    index = index + 1
                    nums[index] = nums[i]
            return index + 1
