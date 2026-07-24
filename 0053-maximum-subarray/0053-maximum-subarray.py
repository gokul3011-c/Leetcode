class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        currentsum = nums[0]
        res = nums[0]
        i =0
        for i in range(1,n):
            currentsum = max(currentsum + nums[i],nums[i])
            res = max(res,currentsum)

        return res
        