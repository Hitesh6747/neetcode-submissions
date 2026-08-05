class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        siu={}
        if (len(s))!=(len(t)):
            return False
        for word in s:
            if word in siu:
                siu[word]+=1
            else:
                siu[word]=1
        for word in t:
            if word in siu:
                siu[word]-=1
            else:
                return False
        for word in siu:    
            if siu[word]!=0:
                 return False
        return True