class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

s = Solution()
nums = [1, 3, 2]
s.nextPermutation(nums)
print(nums)

'''关键在于理解题目中：下一个排列到底是什么意思，这里想清楚了才能
明白：
    从右往左找第一个下降点，再将下降点和右侧第一个大于该点的位置与下降点互换数值，
    最后把i+1,len(nums)-1这个区间弄成升序。这个升序就是下一个排序的精髓'''