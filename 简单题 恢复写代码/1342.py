class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step = 0
        while(num):
            if num%2 == 0:
                step += 1
                num /= 2
            else:
                step += 1
                num -= 1
        
        return step