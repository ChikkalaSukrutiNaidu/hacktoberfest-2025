class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return(-1)
        i=haystack.find(needle,0)
        if i!=-1:
            return(i)
        else:
            return(-1)
