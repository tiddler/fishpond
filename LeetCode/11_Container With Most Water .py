class Solution:
    # @return an integer
    def maxArea(self, height):
        length = len(height)
        low = 0
        high = length - 1
        max_val = 0
        while low < high:
            temp = min(height[low], height[high]) * (high - low)
            max_val = max_val if max_val > temp else temp
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_val