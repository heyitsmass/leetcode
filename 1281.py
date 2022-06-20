class Solution:
  def subtractProductAndSum(self, n: int) -> int:
    prod = 1
    sum = 0 

    for tmp in str(n): 
      num = int(tmp) 
      prod *= num 
      sum += num  
    
    return prod - sum  