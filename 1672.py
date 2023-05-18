class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(accounts)):
            welth = sum(accounts[i])
            if welth > ans:
                ans = welth
        return ans
