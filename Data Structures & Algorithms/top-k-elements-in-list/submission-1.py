class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fuck = {}
        for i in nums:
            if i in fuck:
                fuck[i]+=1
            else:
                 fuck[i]=1
        
        freq =[[] for i in range(len(nums)+1)]
        for key,values in fuck.items():
            freq[values].append(key)
        result =[]
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result)==k:
                    return result

        
        