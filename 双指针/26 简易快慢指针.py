class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            else:
                fast += 1

        n = slow + 1
        return n