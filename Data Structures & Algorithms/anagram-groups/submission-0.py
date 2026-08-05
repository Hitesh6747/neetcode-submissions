class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dick = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in dick:
                dick[key].append(word)
            else:
                dick[key]=[word]
        return list(dick.values())


        