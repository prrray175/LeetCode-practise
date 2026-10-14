"""class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        now = dict.fromkeys(p,0) #p中有可能存在重复字符
        need = now.copy()
        for each in p:
            need[each] += 1 #统计p中字符出现的次数
        lens = len(p)
        times = lens
        left = 0
        result = []
        for right, ch in enumerate(s):
            if ch not in need:
                left = right + 1
                times = lens
                for k in now:
                    now[k] = 0
                continue
            elif now[ch] == need[ch] : #该字符已经存满，此字符第一次出现位置之前所有值作废
                while s[left] != ch and left < right: #若need[ch] = 1，left 会移到当前right 的前一个位置
                    if s[left] in now:
                        now[s[left]] -= 1
                        times += 1
                    left += 1
                left += 1
            else:
                now[ch] += 1
                times -= 1
            if right - left + 1 == lens: #字串长度已达标准
                if times == 0:
                    result.append(left)
                now[s[left]] -= 1
                left += 1
                times += 1
        return result
s = "abaacbabc"
p = "abc"
print(Solution().findAnagrams(s, p))"""

"""思路可行，但每次清空计数器的操作略显冗余
   新学了Counter,以后可以省略统计出现次数这一步骤"""

#改进方案:
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        k = len(p)
        window = Counter()
        left = 0
        result = []
        for right, ch in enumerate(s):
            window[ch] += 1
            if right - left + 1 > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            if window == need:
                result.append(left)
        return result
"""改进思路：采用一个空字典window，整体比较两个字典need和window，当window整体等于need时，也就证明
此时字串满足题意
del去空字符省事，后面再出现时会自动重新生成一对键值。
代码精简，但会牺牲一些执行用时
"""