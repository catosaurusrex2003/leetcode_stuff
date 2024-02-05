class Solution:
    def findMin(self, nums):
        length = len(nums)
        left = 0
        right = length - 1
        ans = nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                ans = min(ans,nums[left])
                break
            mid = (left + right) // 2
            ans = min(ans,nums[mid])
            if nums[mid] >= nums[left]:
                left = mid +1
            else:
                right = mid-1
        
        return ans

obj = Solution()

method = obj.findMin([3, 4, 5, 1, 2])
print(method)
