class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowPtr = 0 
        # i represents fast pointer
        for i in range(len(nums)):
            if nums[slowPtr] != nums[i]:
                slowPtr += 1 
                nums[slowPtr] = nums[i]
        return slowPtr + 1
            