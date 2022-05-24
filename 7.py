class Solution:
    def reverse(self, x: int) -> int:
        MAX = pow(2, 31) - 1
        MIN = (MAX + 1) * -1

        if x < MIN or x > MAX: 
            return 0 

        tmp = str(x)[::-1]

        if x < 0: 
            sign = -1 
            tmp = tmp[:-1] 
        else: 
            sign = 1 
        
        tmp = int(tmp) * sign 
            
        return tmp if tmp >= MIN and tmp <= MAX else 0  
