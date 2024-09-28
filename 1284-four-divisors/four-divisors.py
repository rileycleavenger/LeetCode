class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        
        total = 0
        
        for num in nums:
            curr_divs = set()
            for i in range(1, int(1+sqrt(num))):
                if num % i == 0:
                    curr_divs.add(num/i)
                    curr_divs.add(i)
            if len(curr_divs) == 4:
                total += int(sum(curr_divs))
        
        return total
                