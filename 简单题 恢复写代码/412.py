class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []

        for j in range(n):
            i = j+1
            if i%5 == 0:
                if i%3 == 0:
                    ans.append('FizzBuzz')
                else:
                    ans.append('Buzz')
            elif i%3 == 0:
                ans.append('Fizz')
            else:
                ans.append(str(i))
        
        return ans