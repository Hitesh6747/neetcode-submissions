class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        
        sex=[]
        

        while left<=len(nums)-k:
            max=float("-inf")
            for i in range (left,left+k):
                if nums[i]>max:
                    max=nums[i]
            sex.append(max)
            left+=1
        return sex
        