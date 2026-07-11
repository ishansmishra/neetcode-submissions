class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=[x.lower() for x in s if x.isalnum()]
        l,r=0,len(s)-1
        while r>=l:
            if s[r]!=s[l]:
                return False
            r-=1
            l+=1
        return True     