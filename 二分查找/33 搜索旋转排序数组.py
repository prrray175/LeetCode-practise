class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        f = True
        T = False
        if nums[left] < nums[right]:#数组在最后一位旋转，等于没旋转
            T = True
        if target <= nums[right]: #说明target在右半段
            f = False
        while left <= right :
            k = (left + right) // 2
            if nums[k] == target:
                return k

            if nums[k] > nums[n - 1] and not f and not T: #现在的k在左半段而target在右半段
                left = k + 1
                continue
            elif nums[k] < nums[n - 1] and f and not T :#现在的k在右半段而target在左半段
                right = k - 1

                continue
            #移完之后就是正常的二分查找
            if nums[k] > target :#f = True 说明target在左半段
                right = k - 1

            elif nums[k] < target:
                left = k + 1

        return -1
nums = [4,5,6,7,0,1,2]
target = 6
print(Solution().search(nums, target))
"""1、不满足nums = [1, 3],target = 3, 需要考虑数组没旋转和数组最后一位旋转两种情形
   2、需要注意，在判断目前k在哪一段时，应用数组最后一个数值，即nums[n - 1]而非nums[right]。因为right可变"""
"""思路：由于题目要求复杂度为O(logn)很明显是二分查找，通过观察发现，旋转后的数组分为两半，而两段都是递增的。
        故思考，能不能先固定住left或者right，进入到特定的一段中进行正常的二分查找。"""