class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result =[]
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1]+nums[i + 2] + nums[i + 3] > target: #剪枝1
                continue
            elif nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:#剪枝2
                continue
            ttarget = target - nums[i]
            for j in range(i + 1,n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                z = nums[j]
                left = j + 1
                right = n - 1
                if z + nums[j + 1] + nums[j + 2]  > ttarget:
                    break
                while left < right:
                    x, y = nums[left], nums[right]
                    if x + y + z == ttarget:
                        result.append([nums[i], z, x, y])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] ==nums[right + 1]:
                            right -= 1
                    elif x + y + z > ttarget:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    else:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
        return result
sol = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(sol.fourSum(nums, target))

