class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        if n == 1:
            return [0]
        count = 0
        temp =[]
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])
                count+=1
        for j in range(len(temp)):
            nums[j] = temp[j]
        for k in range(count,n):
            nums[k] = 0
        return nums

        
        