class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len1 = 0
        maxlen = 0
        while len1 < len(strs[0]):
            letter = strs[0][len1]
            count = 1
            for j in range(1, len(strs)):
                if strs[j][len1] == letter:
                    count += 1
            if count == len(strs):
                maxlen += 1
                len1 += 1
            else:
                break
        if maxlen != 0:
            return strs[0][:maxlen]
        else:
            return ""