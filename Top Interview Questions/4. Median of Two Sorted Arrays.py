class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        l1 = len(nums1)
        l2 = len(nums2)
        l = l1+l2

        if ((l1+l2) % 2):
            return self.get_median(nums1, nums2, l//2)
        else:
            return (self.get_median(nums1, nums2, l//2) +  self.get_median(nums1, nums2, l//2-1))/2.0
    
    def get_median(self, a, b, idx):

        if not a:
            return b[idx]
        
        if not b:
            return a[idx]
        
        ai = len(a) // 2
        bi = len(b) // 2


        ma = a[ai]
        mb = b[bi]

        if ma > mb:
            ma, mb = mb, ma 
            ai, bi = bi, ai
            a, b = b, a

        max_possible_ma = ai + bi

        if idx > max_possible_ma:
            return self.get_median(a[ai+1:], b, idx-ai-1)
        else:
            return self.get_median(a, b[:bi], idx)
        






