class Solution:
    def firstUniqChar(self, s: str) -> int:
        track = {}
        for a in s:
            track[a] = track.get(a, 0) + 1
        for i in range(len(s)):
            if track[s[i]] == 1:
                return i
        return -1


obj = Solution()
method = obj.solution("")
print(method)
