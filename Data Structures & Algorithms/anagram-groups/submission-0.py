class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}

        for i in range(len(strs)):
            sortedWord = "".join(sorted(strs[i]))
            if sortedWord not in strMap:
                strMap[sortedWord] = [strs[i]]
            else:
                strMap[sortedWord].append(strs[i])
        
        return list(strMap.values())