class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        num = 0
        minl = 0
        right = 0
        while right < len(nums):
            num += nums[right]
            if num < target:
                right += 1
                continue
            else:
                while num >= target:
                    if minl == 0:
                        minl = right - left + 1
                    else:
                        minl = min(minl, right - left + 1)
                    num -= nums[left]
                    left += 1
            right += 1
        return minl

#双指针加滑动窗口，比较简单