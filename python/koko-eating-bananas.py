class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right
        while left <= right:
            speed = (left+right)//2
            hours = 0

            for height in piles:
                hours += math.ceil(height/speed)
            if hours <= h:
                ans = min(ans,speed)
                right = speed -1
            else:
                left = speed + 1
        return ans
