class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        track=[]
        res=[]
        def backtrack(start,remaining):
            if remaining==0:
                res.append(track.copy()) 
                return 
            if remaining<0:
                return
            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > remaining:
                    break

                track.append(candidates[i])

                backtrack(i + 1, remaining - candidates[i])

                track.pop()
        backtrack(0,target)
        return res