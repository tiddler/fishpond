class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        index = 0
        ans = ''
        if len(strs) == 0:
            return ans
        while True:
            if index == len(strs[0]):
                return ans
            if len(strs[0]) > 0:
                char = strs[0][index]
            for str in strs:
                if len(str) == 0:
                    return ans
                if index == len(str):
                    return ans
                if str[index] != char:
                    return ans
            ans += char
            index += 1
        return ans