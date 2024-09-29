class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n < 2:
            return 0
        
        composites = [False]*n
        composites[0], composites[1] = True, True
        
        for i in range(2, int(sqrt(n)+1)):
            if not composites[i]:
                for j in range(i*i, n, i):
                    composites[j] = True
        
        count = 0
        for x in composites:
            if not x: count += 1
                
        return count