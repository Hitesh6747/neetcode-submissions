class Solution:
    def isPalindrome(self, s: str) -> bool:
        result="".join(c for c in s if c.isalnum())
        result1 = result.lower()
      
        if result1==result1[::-1]:
            return True 
        return False
        
        