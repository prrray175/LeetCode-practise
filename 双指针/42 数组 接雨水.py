class Solution:
    def trap(self, height: list[int]) -> int:
        #先比较左边的值和右边的值哪个大，选择较小的那边，此时较小边以外的最大值，必定小于较大边以外的最大值
        n = len(height)
        left = 0
        right = n - 1
        maxleft = 0
        maxright = 0
        v = 0
        while left < right:
            if height[left] < height[right]:
                maxleft = max(maxleft, height[left])
                v += maxleft - height[left]
                left += 1
            else:
                maxright = max(maxright, height[right])
                v += maxright - height[right]
                right -= 1
        return v
height = [4,2,0,3,2,5]
print(Solution().trap(height))
"""归纳： 假设进入 if 前 leftMax ≤ rightMax 成立。

因为进 if 的条件是 height[left] < height[right]，而 rightMax ≥ height[right]，所以 height[left] < rightMax。
更新 leftMax = max(旧leftMax, height[left])，而"旧 leftMax ≤ rightMax"（归纳假设）且 "height[left] < rightMax"，所以新 leftMax 依然 ≤ rightMax。
不变式保持成立。对称地，else 分支处理 right 时，恒有 rightMax ≤ leftMax。"""