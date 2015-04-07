'''
After writing some examples, it is easy to find that it is a loop. The length of loop is 2 * nRows - 2
if there is another char in the the same loop that locates at the some line, the relasionship is
x1, x2 are the index of the two numbers
x1 + x2 = loop_length + loop_length * 2 * loop_times
'''
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 1:
            return s
        loop = 2 * nRows - 2
        ans = ''
        for x in xrange(0, nRows):
            loop_num = 0  #index the kth loop it comes
            index = x + loop_num * loop
            while index < len(s):
                ans += s[index]
                other_index = loop + loop_num * 2 * loop - index  #judge whether there is another char in the line
                if other_index < len(s) and other_index < (1 + loop_num) * loop and other_index > loop_num * loop + nRows - 1:
                    ans += s[other_index]
                loop_num += 1
                index = x + loop_num * loop
        return ans
