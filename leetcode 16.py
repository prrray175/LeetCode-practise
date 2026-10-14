class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        temp = 0
        min = float('inf')
        result = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            x = nums[i]
            left = i + 1
            right = n - 1
            while left < right:
                y = nums[left]
                z = nums[right]
                temp = x + y + z
                if temp == target:
                    result = target
                    return result
                if abs(temp - target) < min:
                    min = abs(temp - target)
                    result = temp
                    if (temp - target) > 0:
                        right -= 1
                    else:
                        left += 1
                elif (temp - target) > 0:  # 三数之和大于target
                    right -= 1

                else:
                    left += 1

        return result
print(Solution().threeSumClosest([1,3,4,7,8,9], 15))
