'''
Symbol  Value
I   1
V   5
X   10
L   50
C   100
D   500
M   1,000

4 = 5 - 1
9 = 10 - 1

'''
class Solution:
    # @return an integer
    def romanToInt(self, s):
        change_table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        index = 0
        while index < len(s):
            if index + 1 < len(s) and change_table[s[index + 1]] > change_table[s[index]]:
                ans += change_table[s[index + 1]] - change_table[s[index]]
                index += 2
            else:
                ans += change_table[s[index]]
                index += 1
        return ans