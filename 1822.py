class Solution:
    def arraySign(self, nums:list) -> int:
      prod = 1 
      for num in nums: 
        prod *= num 

      if not prod: 
        return 0  
      elif prod < 0: 
        return -1 
      else: 
        return 1 