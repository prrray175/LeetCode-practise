class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        slow = 0
        fast = 0
        k = 0
        while fast < n:
            if nums[fast] != val:
                k += 1
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return k
