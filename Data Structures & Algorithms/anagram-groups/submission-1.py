class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}
        result = []
        for word in range(len(strs)):
            sortedWord = "".join(sorted(strs[word]))
            if sortedWord not in wordMap:
                wordMap[sortedWord] = [strs[word]]
            else:
                wordMap[sortedWord].append(strs[word])

        return list(wordMap.values())
