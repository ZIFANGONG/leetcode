class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    dp[i][j] = True
                else:
                    dp[i][j] = False







        max_len = 1
        max_start = 0
        max_end = 0

        for i in range(n-1, -1, -1):
            for j in range(i, n, 1):

                if s[i] == s[j]:
                    if j-1 >= i+1:
                        if dp[i+1][j-1]:
                            dp[i][j] = True
                    else:
                        dp[i][j] = True

                
                if dp[i][j] and j-i+1 > max_len:

                    max_len = j-i+1
                    max_start = i
                    max_end = j
        


        return(s[max_start : max_end+1])