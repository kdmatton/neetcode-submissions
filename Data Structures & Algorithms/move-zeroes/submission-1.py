class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[slow], nums[i] = nums[i], nums[slow]
                slow += 1
        return nums
        