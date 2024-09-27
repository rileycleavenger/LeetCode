class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        
        for i in nums:
            curr_divs = set()
            for j in range(1, int(sqrt(i)+1)):
                if i % j == 0:
                    curr_divs.add(i/j)
                    curr_divs.add(j)
    
            if len(curr_divs) == 4:
                total += int(sum(curr_divs))

        return total
                
        