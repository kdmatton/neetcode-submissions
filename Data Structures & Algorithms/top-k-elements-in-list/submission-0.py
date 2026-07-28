class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}

        for i in range(len(nums)):
            if nums[i] not in numsMap:
                numsMap[nums[i]] = 1
            else:
                numsMap[nums[i]] += 1

        sortedData = dict(sorted(numsMap.items(), key=lambda item: item[1], reverse=True))
        return list(sortedData.keys())[:k]
        