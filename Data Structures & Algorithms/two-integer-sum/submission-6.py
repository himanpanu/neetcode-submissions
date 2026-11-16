class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, item in enumerate(nums):
            if(target-item not in nums[(i+1):]):
                continue
            targetItem = nums.index(target - item)
            if(targetItem == i):
                targetItem = (nums[(targetItem+1):]).index(target - item) + (targetItem+1)
           
            return [i, targetItem] 
