class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        mat = set(nums)
        longl = 0
        for i in nums:
            if i-1  not in mat:
                long = 1
                temp = i
                while temp + 1 in mat:
                    long += 1
                    temp += 1
                longl = max(longl, long)
                if longl >= len(nums) / 2:
                    break
        return longl
s = Solution()
print(s.longestConsecutive([1,2,3,4,5]))
'''思路：Hashset可以将列表中的元素自动去重后转化成集合形式，这样判断一个数是否在这个集合里时，时间复杂度就是O(1),i in nums
    这道题的关键点在于，要找到列表中哪个元素是一段连续序列的起点。因为如果每个数都当作起点往后判断一下后续有序数字的个数，那么
    整个程序运行需要的时间就很长了。
    所以可以根据：排头元素i的i-1一定不在集合中。实现找到排头兵后再进行长度的判断'''