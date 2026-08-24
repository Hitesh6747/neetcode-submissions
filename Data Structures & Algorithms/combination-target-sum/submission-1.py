class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        track=[]
        res=[]
        def backtrack(i,remaining):
            if remaining==0:
                res.append(track.copy()) 
                return 
            if remaining<0:
                return
            if i>=len(nums):
                return
            track.append(nums[i])
            backtrack(i,remaining-nums[i])

            track.pop()
            backtrack(i+1,remaining)
        backtrack(0,target)
        return res 

            
        