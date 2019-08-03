class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        elif val not in nums:
            return len(nums)
        else:
            n_occurrences = nums.count(val)
            for i in range(n_occurrences):
                val_index = nums.index(val)
                del nums[val_index]
            return len(nums)
                
            # n_occurrences = nums.count(val)
            # removed_list = [val for i in range(n_occurrences)]
            # nums = [x for x in nums if x not in removed_list]
            # return len(nums)
        
            # nums = sorted(nums)
            # begin = nums.index(val)
            # n_occurrences = nums.count(val)
            # del nums[begin:begin + n_occurrences]
            # return len(nums) 
