class Solution:
    # @return a tuple, (index1, index2)
    '''
        Normal search in list is O(n), which will cause time-out
        Therefore, "set" is needed since judging whether a num in set is O(1)
    '''
    def twoSum(self, num, target):
        my_set = set(num)
        index1 = -1
        index2 = -1
        for x in num:
            if (target - x) in my_set:
                index1 = num.index(x)
                for index, val in enumerate(num):
                    if (val == target - x) & (index != index1):
                        index2 = index
                        break
                if index2 == -1:
                    continue
                temp = index1 + index2
                index1 = index1 if index1 < index2 else index2
                index2 = temp - index1
                return (index1 + 1, index2 + 1)