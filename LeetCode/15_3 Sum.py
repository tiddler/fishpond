class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        count = {}    #record the count of each value
        ans = []
        for val in num:
            if count.has_key(val):
                count[val] += 1
            else:
                count[val] = 1
        for key1 in count:
            for key2 in count:
                key3 = 0 - key1 - key2
                if count.has_key(key3):
                    temp1 = count[key1]
                    temp2 = count[key2]
                    temp3 = count[key3]
                    count[key1] -= 1
                    count[key2] -= 1
                    count[key3] -= 1
                    if count[key1] >= 0 and count[key2] >= 0 and count[key3] >= 0:
                        if sorted([key1, key2, key3]) not in ans:
                            ans.append(sorted([key1, key2, key3]))
                    count[key1] = temp1
                    count[key2] = temp2
                    count[key3] = temp3
        return ans