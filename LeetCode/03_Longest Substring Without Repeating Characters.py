class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        maxlength = 0
        begin_index = 0
        check_index = 0
        end_index = 0

        while check_index < len(s):
            repeated_index = self.checkRepeated(s[begin_index : end_index], s[check_index])
            if repeated_index != -1:
                begin_index += repeated_index + 1
            else:
                end_index = check_index + 1
                check_index += 1
                if end_index - begin_index > maxlength:
                    maxlength = end_index - begin_index

        return maxlength

    def checkRepeated(self, s, target):
        for index, char in enumerate(s):
            if char == target:
                return index
        return -1