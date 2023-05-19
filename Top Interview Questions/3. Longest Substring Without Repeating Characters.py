class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        l = 0
        length = 0

        for r in range(len(s)):
            char = s[r]

            if char not in dic:
                length = max(length, r-l+1)
            else:
                if dic[char] < l:
                    length = max(length, r-l+1)
                else:
                    l = dic[char] + 1
                
            
            dic[char] = r
        
        return length