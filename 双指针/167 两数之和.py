class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        while left <= right:
            t = numbers[left] + numbers[right]
            if t == target:
                return ([left + 1, right + 1])
            elif t < target:
                left += 1
            else:
                right -= 1
