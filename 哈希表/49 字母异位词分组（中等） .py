class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        hs = {}
        for each in strs:
            key = tuple(sorted(each))
            if key not in hs:
                hs[key] = []
            hs[key].append(each)
        ans = []
        for word in hs:
            ans.append(hs[word])
        return ans
s=Solution()
strs = ['a']
print(s.groupAnagrams(strs))
#直接用sorted找出不同字符串的字母组合，如果两个字符串sorted之后的结果相同，那么显然这两个字符串互为字母异位词
#hs字典的键直接使用字母的不同排列，这也是我一开始没有想到的部分