class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        i = 0
        result = ""
        lens = 0
        while i < len(s):
            if s[i] in result:
                for j in range(lens-1,-1,-1):
                    if result[j] == s[i]:
                        if j == lens-1:
                            result = ""
                            lens = 0
                        else:
                            result = result[j + 1:]
                            lens -= j + 1
                        break
                result += s[i]
            else:
                result += s[i]
            lens += 1
            i += 1
            maxl = max(maxl, lens)
        return maxl
#这一思路较为复杂，时间复杂度较高
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))

"""class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {} #字符最后一次出现的位置
        left = 0
        ans = 0
        for  right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1 #跳到最后一个重复字符的后一个位置
            last[ch] = right
            ans = max(ans, right - left + 1)
        return ans"""
#哈希表提升了运行效率