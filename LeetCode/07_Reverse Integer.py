class Solution:
    # @return an integer
    def reverse(self, x):
        ans = str(abs(x))[::-1]
        if x < 0:
            ans = '-' + ans
        ans = int(ans)
        if (ans >= 2**31) or (ans < -(2**31)):
            return 0
        return int(ans)