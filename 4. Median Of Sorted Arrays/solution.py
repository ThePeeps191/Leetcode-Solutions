class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        n.sort()
        if (len(n) % 2) == 1:
            i = int(len(n) / 2 - 0.5)
            return float(n[i])
        else:
            j = n[len(n) // 2] + n[len(n) // 2 - 1]
            return float(j / 2)
