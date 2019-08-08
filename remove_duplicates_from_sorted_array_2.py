class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        else:
            nums_dict = {}
            index = 0
            for i in nums:
                if i not in nums_dict:
                    nums_dict[i] = 1
                elif nums_dict[i] <= 1:
                    nums_dict[i] += 1
                else:
                    continue
                    
                nums[index] = i
                index += 1
            return index
