'''已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。'''


class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        Flag = False #表示当前left初次在左半段
        if nums[left] < nums[right]:#旋转了n次
            return nums[0]
        times = 0
        while left <= right :
            times += 1
            mid = (left+right)//2
            if nums[mid] > nums[right] and not Flag:
                left = mid + 1
                continue
            elif nums[left]>nums[right] and Flag:
                return nums[left + 1]
            elif nums[mid] < nums[right] :
                if not Flag:
                    left = mid
                    Flag = True
                else:
                    left -= 1
                continue
            else:
                return nums[left]


nums = [2,3,4,5,6,1]
s = Solution()
print(s.findMin(nums))
'''想复杂了，模板：class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1   # mid 在左半段(较大段)，最小值在右边
            else:
                right = mid      # mid 在右半段(较小段)，最小值在 [left, mid]
        return nums[left]'''