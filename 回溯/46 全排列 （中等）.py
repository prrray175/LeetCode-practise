class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(x):
            if x == len(nums) -1:
                res.append(list(nums))
            for i in range(x, len(nums)):
                nums[i], nums[x] = nums[x], nums[i]
                dfs(x + 1)
                nums[i], nums[x] = nums[x], nums[i]
            return res
        res = []
        return dfs(0)