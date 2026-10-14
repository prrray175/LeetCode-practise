class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = -1
        end = -1
        Len = 0
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        #left的值即为元素的开始位置
        start = left
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        # left - 1即为元素的结束位置
        end = left - 1
        if start > end:
            return [-1, -1]
        else:
            return [start, end]
nums = []
target = 0
print(Solution().searchRange(nums, target))
#因为一个元素出现多次，我无法确定查找到的元素是否是第一个出现的
'''思路：使用两次二分查找，分别查找第一个元素的位置和最后一个元素的位置'''