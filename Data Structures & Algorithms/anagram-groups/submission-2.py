class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm=defaultdict(list)
        for word in strs:
            charlist=[0]*26
            for x in word:
                charlist[ord(x)-97]+=1
            hm[tuple(charlist)].append(word)
        return list(hm.values())

