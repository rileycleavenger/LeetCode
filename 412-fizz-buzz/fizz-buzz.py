class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        res = [""]*(n+1)
        
        for i in range(1, n+1):
            
            if i % 15 == 0:
                res[i] = "FizzBuzz"
            elif i % 5 == 0:
                res[i] = "Buzz"
            elif i % 3 == 0:
                res[i] = "Fizz"
            else:
                res[i] = str(i)
        
        return res[1:]