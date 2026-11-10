class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x=len(s)
        if x!=len(t):
            return False
        
        a=[0]*26
        for i in range(x):
            a[ord(s[i])-97]+=1
            a[ord(t[i])-97]-=1
        
        for x in a:
            if x!=0:
                return False
        return True