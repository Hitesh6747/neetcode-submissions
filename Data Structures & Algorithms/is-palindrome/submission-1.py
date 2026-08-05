class Solution:
    def isPalindrome(self, s: str) -> bool:
        result="".join(c for c in s if c.isalnum())
        result1 = result.lower()
      
        left =0
        right=len(result1)-1
        while left<right:
            if result1[left]!=result1[right]:
                return False
            left+=1
            right-=1
        return True
        