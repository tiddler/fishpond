class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        digit = 0
        temp = x

        while temp > 0:
            temp = temp / 10
            digit += 1

        temp = 0
        target = (digit + 1) // 2
        while digit > target:
            pal_l = x // (10 ** (digit - 1)) % 10
            pal_r = x % (10 ** (temp + 1)) // (10 ** temp)
            temp += 1
            digit -= 1
            if pal_l != pal_r:
                return False
        return True