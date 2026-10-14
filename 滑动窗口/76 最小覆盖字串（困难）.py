"""t = "abcba"
s = "abcasdhnfafsjadcsdb"
last = dict.fromkeys(t,0)
start = {c:[] for c in t}
minl = ""
for each in t:
    last[each] += 1 #这样就能统计出每个字符需要的个数了
#判满条件:sum(last.values()) == 0
for right, ch in enumerate(s):
    if ch not in last:
        continue
    if last[ch] == 0:
        start[ch].pop(0)
        start[ch].append(right)
    else:
        last[ch] -= 1
        start[ch].append(right)
    if sum(last.values()) == 0:
        left = min(v[0] for v in start.values())
        if minl == "" or right - left + 1 < len(minl):
            minl = s[left:right+1]
print(minl)"""
"""我第一次的思路是分别创建两个字典，一个字典是存放每个字符出现的位置，另一个字典存放每个字符需要的次数。跑是能跑对，但是效率有点低。
运行时间有点长，占用内存也有点大"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = dict.fromkeys(t, 0) #记录每个字符需要出现的次数
        for each in t:
            need[each] += 1
        now = dict.fromkeys(t, 0)
        times = len(t)
        left = 0
        minl = ""
        g_left = 0
        g_right = 0
        flag1 = False
        for right, ch in enumerate(s):
            if ch not in need: continue
            if now[ch] <= need[ch] - 1:
                times -= 1
                now[ch] += 1

                if times == 0: #窗口包含了t中所有字符
                    flag1 = True
                    while times == 0:
                        if s[left] not in need:
                            left += 1
                        elif now[s[left]] - 1 >= need[s[left]]: #删除一个字符无影响
                            now[s[left]] -= 1
                            left += 1

                        elif now[s[left]] == need[s[left]]:
                            break
                #此时的left已经移到了最小字符串的开头
                    if g_right - g_left  == 0 or right - left  < g_right - g_left :
                        g_left = left
                        g_right = right
                    now[s[left]] -= 1
                    left += 1
                    times += 1

            else:now[ch] += 1
        if flag1 == False:
            return ""
        minl = s[g_left : g_right + 1]
        return minl

s = "abadsadad"
t = "k"
print(Solution().minWindow(s, t))
"""此乃吾的第二版，省了很多内存空间。最大的改变是，我使用了times这个变量来判断字串是否符合条件。
一个数字（还欠多少 / 达标几类）就能替掉一次全局扫描,因为覆盖状态的变化只和刚进刚出的那个字符有关；
左指针只往一个方向走,所以"一直缩到不能再缩"的总代价是摊还 O(n),不是每一步都贵。"""