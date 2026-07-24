class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = {}
        count = 1
        nums.sort()
        for i in range(n):
            if i != n-1:

                if nums[i] == nums[i+1]:
                    count+=1
                else:
                    cnt[nums[i]] = count
                    count = 1
            else:
                cnt[nums[i]] = count
        sorted_cnt = dict(sorted(cnt.items(), key=lambda x: x[1]))
        return list(sorted_cnt.keys())[-1]
        