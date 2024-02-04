class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sizeS = len(s)
        sizeT = len(t)
        sIndex = 0
        tIndex = 0
        if not sizeS:
            return True
        # for i in range(sizeT):
        #     if sIndex < sizeS and s[sIndex] == t[i] :
        #         sIndex += 1
        while tIndex < sizeT:
            if sIndex < sizeS and s[sIndex] == t[tIndex]:
                sIndex += 1
            tIndex+=1

        return sIndex == sizeS


something = Solution()
# something.isSubsequence("","ahbgdc")
# yes = something.isSubsequence("abc", "ahbgdc")
yes = something.isSubsequence("b", "abc")
print(yes)
