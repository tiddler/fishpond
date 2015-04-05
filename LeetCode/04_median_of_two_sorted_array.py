class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        median_index1 = (len(A) + len(B) + 1) // 2
        median_index2 = (len(A) + len(B) + 2) // 2
        if median_index1 == median_index2:
            return self.findKthElement(A, B, median_index1)
        else:
            return (self.findKthElement(A, B, median_index1) + self.findKthElement(A, B, median_index2)) / 2.0

    def findKthElement(self, A, B, k):
        if len(A) > len(B):
            return self.MySolution(B, A, k)
        if len(A) == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        
        kA = min(k // 2, len(A))
        kB = k - kA

        if A[kA - 1] < B[kB - 1]:
            return self.MySolution(A[kA:], B, k - kA)
        elif A[kA - 1] > B[kB - 1]:
            return self.MySolution(A, B[kB:], k - kB)
        else:
            return A[kA - 1]