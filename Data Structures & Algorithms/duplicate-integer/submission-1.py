class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = {}

        for i in range(len(nums)):
            if nums[i] not in numsMap:
                numsMap[nums[i]] = None
            else:
                return True 
        return False