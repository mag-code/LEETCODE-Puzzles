class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#solution 1 
        if len(s) == len(t):
            d1 = {i:0 for i in s}
            d2 = {i:0 for i in t}
            for i in s:
                d1[i]+=1
            for i in t:
                d2[i]+=1
            if d1==d2:
                return True
            return False
        return False
    def isAnagram(self, s: str, t: str) -> bool:
#solution 2
        if len(s) == len(t):           
            news,newt=sorted(s),sorted(t)
            return True if news == newt else False
