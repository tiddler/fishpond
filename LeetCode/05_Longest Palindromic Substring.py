'''
use the Manacher's Algorithm
'''

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        new_string = self.handleString(s)
        pivot = 0
        index = 0
        left_boundry = 0
        right_boundry = 0

        pal_record = []
        pal_record.extend(new_string)

        while index < len(new_string):
            index_mirror = pivot - (index - pivot) #the mirror point of i

            if right_boundry > index:
                pal_record[index] = min(right_boundry - index, pal_record[index_mirror]) 
            else:
                pal_record[index] = 0

            r = index + pal_record[index]
            l = index - pal_record[index]
            while r < len(new_string) and l >= 0 and new_string[r] == new_string[l]:
                pal_record[index] += 1
                r = index + pal_record[index]
                l = index - pal_record[index]

            if index + pal_record[index] > right_boundry:
                pivot = index
                right_boundry = index + pal_record[index]
            index += 1
        
        max_length = 0
        for index, val in enumerate(pal_record):
            if val > max_length:
                max_length = val
                max_index = index
        ans = ''
        for char in new_string[max_index - max_length + 1 : max_index + max_length - 1]:
            if char != '#':
                ans += char
        return ans

    def handleString(self, s):
        new_string = '#'
        for char in s:
            new_string += char + '#'
        return new_string